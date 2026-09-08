import pandas as pd
import os
from anthropic import Anthropic

# Load your combined data
data = pd.read_csv("olist_combined_for_tableau.csv")

# Recalculate delivery days (same as before)
data["order_purchase_timestamp"] = pd.to_datetime(data["order_purchase_timestamp"])
data["order_delivered_customer_date"] = pd.to_datetime(data["order_delivered_customer_date"])
data["delivery_days"] = (data["order_delivered_customer_date"] - data["order_purchase_timestamp"]).dt.days

# Build a summary of your key findings as plain text
summary_stats = f"""
- Average delivery time: {data['delivery_days'].mean():.1f} days
- Average delivery time for 1-star reviews: {data[data['review_score'] == 1]['delivery_days'].mean():.1f} days
- Average delivery time for 5-star reviews: {data[data['review_score'] == 5]['delivery_days'].mean():.1f} days
- Slowest state: {data.groupby('customer_state')['delivery_days'].mean().idxmax()} ({data.groupby('customer_state')['delivery_days'].mean().max():.1f} days avg)
- Percent of orders that are canceled or unavailable: {(data['order_status'].isin(['canceled','unavailable']).mean()*100):.1f}%
"""

print(summary_stats)

# Send this summary to Claude and ask for a business insight write-up
client = Anthropic()  # automatically reads your ANTHROPIC_API_KEY

message = client.messages.create(
    model="claude-sonnet-4-6",
    max_tokens=500,
    messages=[
        {"role": "user", "content": f"""You are a business analyst. Based on the following summary statistics from an e-commerce company's order data, write a short (3-4 sentence) business insight paragraph, followed by 2-3 concrete recommendations. Be direct and specific, referencing the actual numbers.

{summary_stats}"""}
    ]
)

print("\n--- AI GENERATED INSIGHTS ---\n")
print(message.content[0].text)
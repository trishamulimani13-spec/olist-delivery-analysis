import pandas as pd

# Load the data
orders = pd.read_csv("olist_orders_dataset.csv")
customers = pd.read_csv("olist_customers_dataset.csv")
payments = pd.read_csv("olist_order_payments_dataset.csv")

# Merge orders with customers, so each order knows which customer made it
orders_customers = orders.merge(customers, on="customer_id")

# Merge that with payments, so each order also knows how much was paid
full_data = orders_customers.merge(payments, on="order_id")

print(full_data.head())
print(full_data.shape)
# Reference "today" = the day after the most recent order in the dataset
full_data["order_purchase_timestamp"] = pd.to_datetime(full_data["order_purchase_timestamp"])
reference_date = full_data["order_purchase_timestamp"].max() + pd.Timedelta(days=1)

rfm = full_data.groupby("customer_unique_id").agg(
    recency=("order_purchase_timestamp", lambda x: (reference_date - x.max()).days),
    frequency=("order_id", "nunique"),
    monetary=("payment_value", "sum")
).reset_index()

print(rfm.head())
print(rfm.shape)
# What % of customers are one-time buyers?
one_time = (rfm["frequency"] == 1).mean() * 100
print(f"Percent of customers who ordered only once: {one_time:.1f}%")

# Basic value segment: split monetary spend into 4 quartiles
rfm["value_segment"] = pd.qcut(rfm["monetary"], 4, labels=["Low", "Mid-Low", "Mid-High", "High"])

print(rfm["value_segment"].value_counts())
reviews = pd.read_csv("olist_order_reviews_dataset.csv")

# Merge reviews into your existing full_data (orders + customers + payments)
final_data = full_data.merge(reviews, on="order_id", how="left")

# Save it as one clean file for Tableau
final_data.to_csv("olist_combined_for_tableau.csv", index=False)

print("Saved combined file with shape:", final_data.shape)
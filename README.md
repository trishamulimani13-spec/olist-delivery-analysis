# Olist Delivery Performance & Customer Retention Analysis

An end-to-end analytics project on Olist, a Brazilian e-commerce marketplace, using SQL, Python, Tableau, and an LLM-generated business brief.

## Why this project

I'm a final-year BBA student and wanted a real, hands-on project for my job/masters applications instead of another course certificate. I used Olist's public dataset (~100,000 real orders with customer locations, delivery times, payments, and reviews) to work like an analyst would on a genuine business question.

## What I was trying to find out

- What's actually driving customer dissatisfaction on the platform?
- Is Olist retaining the customers it acquires, or losing them after one order?

## Tools used

- **SQL (SQLite)** — extracting and joining order, customer, and review data (`queries.sql`)
- **Python (pandas)** — merging datasets and building an RFM (Recency, Frequency, Monetary) customer analysis (`analysis.py`)
- **Tableau** — an interactive dashboard visualizing delivery performance by state and its link to review scores
- **Claude (LLM)** — turning summary statistics into a written business brief (`ai_insights.py`)

## Key findings

- Orders with 1-star reviews took **20.8 days** to deliver on average — roughly double the **10.2 days** for 5-star reviews.
- A small number of states are reliably slow (not just small-sample noise) — worth prioritizing for logistics fixes.
- **96.9% of customers ordered only once.** Retention, not acquisition, looks like Olist's core growth problem.
- Only 1.3% of orders were canceled/unavailable — the issue is delivery speed, not fulfillment failure.
- Certain product categories (e.g. office furniture) are rated worse independent of delivery time.

Full write-up with reasoning and recommendations: see the case study document linked in my portfolio.

## Live dashboard

[Add your Tableau Public link here]

## Data source

[Olist Brazilian E-Commerce Public Dataset (Kaggle)](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce)

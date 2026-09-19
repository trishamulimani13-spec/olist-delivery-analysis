# Olist Delivery Performance & Customer Retention Analysis

An end-to-end analytics project on Olist, a brazilian e-commerce marketplace, using SQL, Python, and Tableau, with an LLM-generated business brief.

## Why this project

I'm a final year BBA student, and wanted something substantial that I could actually apply on job/masters applications, not justanother course certificate. Used Olist's public dataset of ~100,000 real orders with customer location, delivery, payment and review data to think through like an analyst and answer a genuine business question.

## What I was trying to uncover

- What are the key drivers of customer dissatisfaction on the platform?
- Is Olist failing to retain customers, or are they one-time buyers?

## Tools used

- **SQLite** — extracting and joining order, customer and review data (`queries.sql`)
- **Python (pandas)** — combining datasets and RFM (recency, frequency, monetary) analysis (`analysis.py`)
- **Tableau** — dashboard visualizing delivery performance by state and its relationship to review score
- **Claude (LLM)** — generating a business brief from summary statistics (`ai_insights.py`)

## Key insights

- Orders with 1-star reviews took on average 20.8 days to deliver, compared to 10.2 days for 5-star reviews.
- A small set of states had consistently poor performance — not random noise, but a signal to investigate.
- 96.9% of customers placed only one order. Acquisition, not retention, is Olist's primary challenge.
- Only 1.3% of orders were canceled or marked unavailable. It's not about order fulfillment, but delivery speed.
- Certain categories had disproportionately negative reviews, independent of delivery time.

The full write-up with deeper analysis and recommendations can be found in the case study document linked in my portfolio.

## Live dashboard

public.tableau.com/app/profile/trisha.mulimani/viz/OlistDeliveryPerformanceCustomerSatisfaction_17897514499990/OlistDeliveryPerformanceCustomerSatisfaction

## Data source

[Olist Brazilian E-Commerce Public Dataset (Kaggle)](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce)

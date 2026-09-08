-- Olist Delivery Performance & Customer Retention Analysis
-- Author: Trisha Mulimani
-- Tool: SQLite (DB Browser for SQLite)
-- Data source: Olist Brazilian E-Commerce Public Dataset (Kaggle)


-- ============================================================
-- Query 1: Order status breakdown
-- What it does: counts how many orders fall into each status
-- (delivered, canceled, shipped, etc.) to get a baseline view
-- of the order pipeline.
-- ============================================================

SELECT order_status, COUNT(*)
FROM orders
GROUP BY order_status;


-- ============================================================
-- Query 2: Average delivery time (overall)
-- What it does: calculates the average number of days between
-- purchase and delivery, for orders that were actually delivered.
-- ============================================================

SELECT order_status,
       AVG(julianday(order_delivered_customer_date) - julianday(order_purchase_timestamp)) AS avg_delivery_days
FROM orders
WHERE order_status = 'delivered'
GROUP BY order_status;


-- ============================================================
-- Query 3: Delivery time vs. review score
-- What it does: joins orders with reviews (matching on order_id)
-- to see whether slower delivery is associated with lower review
-- scores. This was the strongest, clearest finding in the project:
-- 1-star orders took roughly twice as long to deliver as 5-star orders.
-- ============================================================

SELECT r.review_score,
       AVG(julianday(o.order_delivered_customer_date) - julianday(o.order_purchase_timestamp)) AS avg_delivery_days
FROM orders o
JOIN reviews r ON o.order_id = r.order_id
WHERE o.order_status = 'delivered'
GROUP BY r.review_score
ORDER BY r.review_score;


-- ============================================================
-- Query 4: Slowest-delivery states (filtered for reliability)
-- What it does: joins orders with customers to find average
-- delivery time by state, plus a count of orders per state so
-- small, unreliable samples can be distinguished from real,
-- high-volume problem areas.
-- ============================================================

SELECT c.customer_state,
       AVG(julianday(o.order_delivered_customer_date) - julianday(o.order_purchase_timestamp)) AS avg_delivery_days,
       COUNT(*) AS num_orders
FROM orders o
JOIN customers c ON o.customer_id = c.customer_id
WHERE o.order_status = 'delivered'
GROUP BY c.customer_state
ORDER BY avg_delivery_days DESC
LIMIT 10;


-- ============================================================
-- Query 5: Worst-reviewed product categories
-- What it does: joins order_items -> products (for category name)
-- and order_items -> reviews (for score) to find which product
-- categories get rated worst. Filtered to categories with more
-- than 50 reviews so single-digit-review categories don't skew
-- the ranking.
-- ============================================================

SELECT p.product_category_name,
       AVG(r.review_score) AS avg_review_score,
       COUNT(*) AS num_reviews
FROM order_items oi
JOIN products p ON oi.product_id = p.product_id
JOIN reviews r ON oi.order_id = r.order_id
GROUP BY p.product_category_name
HAVING COUNT(*) > 50
ORDER BY avg_review_score ASC
LIMIT 10;

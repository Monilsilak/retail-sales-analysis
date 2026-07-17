-- =========================================================
-- PROJECT: Retail Sales Data Analysis
-- FILE: queries.sql
-- TOOL: MySQL Workbench



-- ---------------------------------------------------------
-- SECTION 1: CREATE DATABASE AND TABLE
-- ---------------------------------------------------------
CREATE DATABASE IF NOT EXISTS retail_sales_db;
USE retail_sales_db;

CREATE TABLE IF NOT EXISTS sales (
    OrderID       VARCHAR(20) PRIMARY KEY,
    OrderDate     DATE,
    CustomerID    VARCHAR(20),
    Region        VARCHAR(20),
    City          VARCHAR(50),
    Category      VARCHAR(50),
    Product       VARCHAR(50),
    Quantity      INT,
    UnitPrice     DECIMAL(10,2),
    DiscountPct   INT,
    Sales         DECIMAL(12,2),
    Cost          DECIMAL(12,2),
    Profit        DECIMAL(12,2),
    PaymentMode   VARCHAR(30)
);



-- Check the data loaded correctly
SELECT * FROM sales LIMIT 10;

-- Count total rows
SELECT COUNT(*) AS total_orders FROM sales;




-- Q1. What is the total sales and profit for each region?
SELECT
    Region,
    SUM(Sales)  AS total_sales,
    SUM(Profit) AS total_profit
FROM sales
GROUP BY Region
ORDER BY total_sales DESC;


-- Q2. Which product category is the most profitable?
SELECT
    Category,
    SUM(Profit) AS total_profit
FROM sales
GROUP BY Category
ORDER BY total_profit DESC;


-- Q3. What are the top 5 best-selling products by quantity sold?
SELECT
    Product,
    SUM(Quantity) AS total_units_sold
FROM sales
GROUP BY Product
ORDER BY total_units_sold DESC
LIMIT 5;


-- Q4. What is the monthly sales trend?
SELECT
    DATE_FORMAT(OrderDate, '%Y-%m') AS month,
    SUM(Sales) AS total_sales
FROM sales
GROUP BY month
ORDER BY month;


-- Q5. Who are the top 10 customers by total spending?
SELECT
    CustomerID,
    SUM(Sales) AS total_spent
FROM sales
GROUP BY CustomerID
ORDER BY total_spent DESC
LIMIT 10;


-- Q6. Which payment mode is used the most?
SELECT
    PaymentMode,
    COUNT(*) AS number_of_orders
FROM sales
GROUP BY PaymentMode
ORDER BY number_of_orders DESC;


-- Q7. What is the average order value per region?
SELECT
    Region,
    ROUND(AVG(Sales), 2) AS avg_order_value
FROM sales
GROUP BY Region
ORDER BY avg_order_value DESC;


-- Q8. Find all orders above the average sale value
-- (this uses a subquery - a nice one to mention in interviews)
SELECT OrderID, CustomerID, Sales
FROM sales
WHERE Sales > (SELECT AVG(Sales) FROM sales)
ORDER BY Sales DESC
LIMIT 10;


-- Q9. Profit margin (%) by category
-- (Profit / Sales * 100), rounded to 2 decimal places
SELECT
    Category,
    ROUND(SUM(Profit) / SUM(Sales) * 100, 2) AS profit_margin_pct
FROM sales
GROUP BY Category
ORDER BY profit_margin_pct DESC;


-- Q10. Which region-category combination sells the most?
SELECT
    Region,
    Category,
    SUM(Sales) AS total_sales
FROM sales
GROUP BY Region, Category
ORDER BY total_sales DESC
LIMIT 10;



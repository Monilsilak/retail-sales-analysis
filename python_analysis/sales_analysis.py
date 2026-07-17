

import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("../data/retail_sales_data.csv")


df["OrderDate"] = pd.to_datetime(df["OrderDate"])
df["Month"] = df["OrderDate"].dt.strftime("%Y-%m")

print("STEP 1 DONE: Data Loaded")
print("Number of rows:", len(df))
print("Columns:", list(df.columns))
print()

# ---------------------------------------------------------
# STEP 2: BASIC DATA CLEANING / CHECKS
# ---------------------------------------------------------

missing_values = df.isnull().sum()
print("STEP 2: Checking for missing values")
print(missing_values)
print()


# ---------------------------------------------------------
# STEP 3: BUSINESS QUESTION 1 - Sales by Region
# ---------------------------------------------------------
sales_by_region = df.groupby("Region")["Sales"].sum().sort_values(ascending=False)
print("STEP 3: Total Sales by Region")
print(sales_by_region)
print()

plt.figure(figsize=(7, 5))
sales_by_region.plot(kind="bar", color="#4472C4")
plt.title("Total Sales by Region")
plt.ylabel("Sales (₹)")
plt.xlabel("Region")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("charts/1_sales_by_region.png")
plt.close()

# ---------------------------------------------------------
# STEP 4: BUSINESS QUESTION 2 - Profit by Category
# ---------------------------------------------------------
profit_by_category = df.groupby("Category")["Profit"].sum().sort_values(ascending=False)
print("STEP 4: Total Profit by Category")
print(profit_by_category)
print()

plt.figure(figsize=(7, 5))
profit_by_category.plot(kind="bar", color="#70AD47")
plt.title("Total Profit by Product Category")
plt.ylabel("Profit (₹)")
plt.xlabel("Category")
plt.xticks(rotation=20)
plt.tight_layout()
plt.savefig("charts/2_profit_by_category.png")
plt.close()

# ---------------------------------------------------------
# STEP 5: BUSINESS QUESTION 3 - Monthly Sales Trend
# ---------------------------------------------------------
monthly_sales = df.groupby("Month")["Sales"].sum().sort_index()
print("STEP 5: Monthly Sales Trend")
print(monthly_sales)
print()

plt.figure(figsize=(9, 5))
monthly_sales.plot(kind="line", marker="o", color="#ED7D31")
plt.title("Monthly Sales Trend (2024)")
plt.ylabel("Sales (₹)")
plt.xlabel("Month")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("charts/3_monthly_sales_trend.png")
plt.close()

# ---------------------------------------------------------
# STEP 6: BUSINESS QUESTION 4 - Top 10 Customers by Sales
# ---------------------------------------------------------
top_customers = df.groupby("CustomerID")["Sales"].sum().sort_values(ascending=False).head(10)
print("STEP 6: Top 10 Customers by Total Sales")
print(top_customers)
print()

plt.figure(figsize=(8, 5))
top_customers.plot(kind="barh", color="#264478")
plt.title("Top 10 Customers by Sales")
plt.xlabel("Sales (₹)")
plt.ylabel("Customer ID")
plt.gca().invert_yaxis()
plt.tight_layout()
plt.savefig("charts/4_top_10_customers.png")
plt.close()

# ---------------------------------------------------------
# STEP 7: BUSINESS QUESTION 5 - Most Used Payment Mode
# ---------------------------------------------------------
payment_counts = df["PaymentMode"].value_counts()
print("STEP 7: Orders by Payment Mode")
print(payment_counts)
print()

plt.figure(figsize=(6, 6))
plt.pie(payment_counts, labels=payment_counts.index, autopct="%1.1f%%", startangle=90)
plt.title("Orders by Payment Mode")
plt.tight_layout()
plt.savefig("charts/5_payment_mode_share.png")
plt.close()

# ---------------------------------------------------------
# STEP 8: SAVE A CLEAN SUMMARY FILE (used later in Excel/Power BI)
# ---------------------------------------------------------
summary = pd.DataFrame({
    "Metric": [
        "Total Orders", "Total Sales", "Total Profit",
        "Average Order Value", "Best Region", "Best Category"
    ],
    "Value": [
        len(df),
        round(df["Sales"].sum(), 2),
        round(df["Profit"].sum(), 2),
        round(df["Sales"].mean(), 2),
        sales_by_region.idxmax(),
        profit_by_category.idxmax(),
    ]
})
summary.to_csv("summary_metrics.csv", index=False)

print("ALL DONE! 5 charts saved in the 'charts' folder.")
print("A summary_metrics.csv file was also created.")

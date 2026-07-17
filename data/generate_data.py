
import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

random.seed(42)
np.random.seed(42)

n_rows = 1000

categories = {
    "Electronics": ["Headphones", "Smartphone", "Laptop", "Smartwatch", "Tablet"],
    "Clothing": ["T-Shirt", "Jeans", "Jacket", "Shoes", "Cap"],
    "Home & Kitchen": ["Mixer", "Cookware Set", "Vacuum Cleaner", "Bedsheet", "Lamp"],
    "Beauty": ["Face Cream", "Shampoo", "Perfume", "Lipstick", "Sunscreen"],
    "Sports": ["Cricket Bat", "Football", "Yoga Mat", "Dumbbells", "Running Shoes"],
}

regions = ["North", "South", "East", "West"]
cities = {
    "North": ["Delhi", "Chandigarh", "Lucknow"],
    "South": ["Bengaluru", "Chennai", "Hyderabad"],
    "East": ["Kolkata", "Patna", "Bhubaneswar"],
    "West": ["Mumbai", "Ahmedabad", "Pune"],
}

payment_modes = ["Credit Card", "Debit Card", "UPI", "Cash on Delivery", "Net Banking"]

start_date = datetime(2024, 1, 1)
end_date = datetime(2024, 12, 31)
date_range_days = (end_date - start_date).days

rows = []
for i in range(1, n_rows + 1):
    category = random.choice(list(categories.keys()))
    product = random.choice(categories[category])
    region = random.choice(regions)
    city = random.choice(cities[region])
    order_date = start_date + timedelta(days=random.randint(0, date_range_days))
    quantity = random.randint(1, 6)

    base_prices = {
        "Electronics": (1500, 60000),
        "Clothing": (300, 3500),
        "Home & Kitchen": (500, 12000),
        "Beauty": (150, 2500),
        "Sports": (400, 8000),
    }
    low, high = base_prices[category]
    unit_price = round(random.uniform(low, high), 2)
    sales = round(unit_price * quantity, 2)
    cost_ratio = random.uniform(0.55, 0.8)
    cost = round(sales * cost_ratio, 2)
    profit = round(sales - cost, 2)
    discount_pct = random.choice([0, 0, 0, 5, 10, 15, 20])
    payment_mode = random.choice(payment_modes)
    customer_id = f"CUST{random.randint(1000, 1200)}"

    rows.append({
        "OrderID": f"ORD{i:05d}",
        "OrderDate": order_date.strftime("%Y-%m-%d"),
        "CustomerID": customer_id,
        "Region": region,
        "City": city,
        "Category": category,
        "Product": product,
        "Quantity": quantity,
        "UnitPrice": unit_price,
        "DiscountPct": discount_pct,
        "Sales": sales,
        "Cost": cost,
        "Profit": profit,
        "PaymentMode": payment_mode,
    })

df = pd.DataFrame(rows)
df.to_csv("/home/claude/retail_sales_project/data/retail_sales_data.csv", index=False)
print("Generated", len(df), "rows")
print(df.head())

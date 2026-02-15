#!/usr/bin/env python3
"""
Atliq Hardware Dataset Generator
Creates 5 CSV files for Business Insights 360 Project
"""

import pandas as pd
import numpy as np
from datetime import datetime, timedelta

print("\n" + "="*60)
print("   ATLIQ HARDWARE DATASET GENERATOR")
print("="*60 + "\n")

# Set random seed for reproducibility
np.random.seed(42)

# ============================================
# 1. CREATE PRODUCTS TABLE
# ============================================
print("📦 Creating Products Table...")

categories = ['Laptop', 'Desktop', 'Mouse', 'Keyboard', 'Monitor', 'Accessories']
brands = ['Dell', 'HP', 'Lenovo', 'Apple', 'Asus', 'Samsung', 'Logitech']
variants = ['Standard', 'Premium', 'Budget', 'Pro']

products_data = []

for i in range(1, 51):  # 50 products
    category = np.random.choice(categories)
    brand = np.random.choice(brands)
    
    # Set realistic prices based on category
    if category == 'Laptop':
        cost = np.random.randint(30000, 80000)
    elif category == 'Desktop':
        cost = np.random.randint(25000, 70000)
    elif category == 'Monitor':
        cost = np.random.randint(8000, 40000)
    elif category == 'Keyboard':
        cost = np.random.randint(500, 5000)
    elif category == 'Mouse':
        cost = np.random.randint(300, 3000)
    else:  # Accessories
        cost = np.random.randint(200, 2000)
    
    product = {
        'product_code': f'P{i:03d}',
        'product_name': f'{brand} {category} {np.random.choice(variants)}',
        'category': category,
        'variant': np.random.choice(variants),
        'cost_price': cost
    }
    products_data.append(product)

df_products = pd.DataFrame(products_data)
df_products.to_csv('dim_product.csv', index=False)
print(f"   ✅ dim_product.csv created ({len(df_products)} products)")

# ============================================
# 2. CREATE CUSTOMERS TABLE
# ============================================
print("\n👥 Creating Customers Table...")

platforms = ['Brick & Mortar', 'E-Commerce']
channels = ['Retailer', 'Direct', 'Distributor']
markets = ['India', 'USA', 'Australia', 'Japan', 'South Korea']
indian_states = ['Maharashtra', 'Karnataka', 'Tamil Nadu', 'Delhi', 'Gujarat', 
                 'Uttar Pradesh', 'West Bengal', 'Rajasthan']
us_states = ['California', 'New York', 'Texas', 'Florida']

customers_data = []

for i in range(1, 76):  # 75 customers
    market = np.random.choice(markets)
    
    # Assign sub_zone based on market
    if market == 'India':
        sub_zone = np.random.choice(indian_states)
    elif market == 'USA':
        sub_zone = np.random.choice(us_states)
    else:
        sub_zone = 'International'
    
    customer = {
        'customer_code': f'C{i:03d}',
        'customer_name': f'{"Reliance" if i % 5 == 0 else "Store"}_{i}',
        'platform': np.random.choice(platforms),
        'channel': np.random.choice(channels),
        'market': market,
        'sub_zone': sub_zone
    }
    customers_data.append(customer)

df_customers = pd.DataFrame(customers_data)
df_customers.to_csv('dim_customer.csv', index=False)
print(f"   ✅ dim_customer.csv created ({len(df_customers)} customers)")

# ============================================
# 3. CREATE DATE TABLE
# ============================================
print("\n📅 Creating Date Dimension Table...")

start_date = datetime(2020, 1, 1)
end_date = datetime(2023, 12, 31)

dates_data = []
current_date = start_date

while current_date <= end_date:
    # Calculate fiscal year (April to March for India)
    if current_date.month >= 4:
        fiscal_year = current_date.year
    else:
        fiscal_year = current_date.year - 1
    
    # Calculate quarter
    month = current_date.month
    if month in [1, 2, 3]:
        quarter = 'Q4'
    elif month in [4, 5, 6]:
        quarter = 'Q1'
    elif month in [7, 8, 9]:
        quarter = 'Q2'
    else:
        quarter = 'Q3'
    
    date_entry = {
        'date': current_date.strftime('%Y-%m-%d'),
        'fiscal_year': f'FY {fiscal_year}',
        'month': current_date.strftime('%B'),
        'month_number': current_date.month,
        'quarter': quarter,
        'year': current_date.year,
        'day_of_week': current_date.strftime('%A')
    }
    dates_data.append(date_entry)
    current_date += timedelta(days=1)

df_dates = pd.DataFrame(dates_data)
df_dates.to_csv('dim_date.csv', index=False)
print(f"   ✅ dim_date.csv created ({len(df_dates)} days)")

# ============================================
# 4. CREATE SALES TABLE (FACT TABLE)
# ============================================
print("\n💰 Creating Sales Transactions Table...")

sales_data = []
product_codes = df_products['product_code'].tolist()
customer_codes = df_customers['customer_code'].tolist()

# Generate 10,000 realistic transactions
for transaction_id in range(1, 10001):
    # Random date within range
    random_days = np.random.randint(0, (end_date - start_date).days + 1)
    sale_date = start_date + timedelta(days=random_days)
    
    # Select random product and customer
    product_code = np.random.choice(product_codes)
    customer_code = np.random.choice(customer_codes)
    
    # Get product cost
    cost_per_unit = df_products[df_products['product_code'] == product_code]['cost_price'].values[0]
    
    # Realistic quantity distribution (most orders are small)
    quantity = np.random.choice(
        [1, 2, 3, 5, 10, 15, 20, 25, 30, 50],
        p=[0.25, 0.20, 0.15, 0.12, 0.10, 0.08, 0.05, 0.03, 0.01, 0.01]
    )
    
    # Calculate revenue (20-40% markup on cost)
    markup = np.random.uniform(1.20, 1.40)
    selling_price = cost_per_unit * markup
    revenue = selling_price * quantity
    total_cost = cost_per_unit * quantity
    
    # Add some discount factor occasionally
    if np.random.random() < 0.15:  # 15% of orders have discount
        discount_pct = np.random.uniform(0.05, 0.15)
        revenue = revenue * (1 - discount_pct)
    
    sale = {
        'transaction_id': f'T{transaction_id:06d}',
        'date': sale_date.strftime('%Y-%m-%d'),
        'product_code': product_code,
        'customer_code': customer_code,
        'sold_quantity': quantity,
        'revenue': round(revenue, 2),
        'cost': round(total_cost, 2),
        'profit': round(revenue - total_cost, 2)
    }
    sales_data.append(sale)

df_sales = pd.DataFrame(sales_data)
df_sales = df_sales.sort_values('date').reset_index(drop=True)
df_sales.to_csv('fact_sales_monthly.csv', index=False)
print(f"   ✅ fact_sales_monthly.csv created ({len(df_sales)} transactions)")

# ============================================
# 5. CREATE TARGETS TABLE
# ============================================
print("\n🎯 Creating Targets Table...")

departments = ['Finance', 'Sales', 'Marketing', 'Supply Chain', 'Operations']
targets_data = []

for year in range(2020, 2024):
    for month in range(1, 13):
        for dept in departments:
            # Base target with some randomness
            base_target = 8000000  # 80 lakhs base
            variation = np.random.uniform(0.7, 1.3)
            
            target = {
                'fiscal_year': f'FY {year}',
                'month': month,
                'month_name': datetime(2020, month, 1).strftime('%B'),
                'department': dept,
                'target_revenue': int(base_target * variation)
            }
            targets_data.append(target)

df_targets = pd.DataFrame(targets_data)
df_targets.to_csv('fact_targets.csv', index=False)
print(f"   ✅ fact_targets.csv created ({len(df_targets)} target records)")

# ============================================
# SUMMARY STATISTICS
# ============================================
print("\n" + "="*60)
print("   ✅ DATASET GENERATION COMPLETE!")
print("="*60 + "\n")

print("📊 SUMMARY:")
print(f"   • Products: {len(df_products)}")
print(f"   • Customers: {len(df_customers)}")
print(f"   • Date Range: {df_sales['date'].min()} to {df_sales['date'].max()}")
print(f"   • Total Transactions: {len(df_sales):,}")
print(f"   • Total Revenue: ₹{df_sales['revenue'].sum():,.0f}")
print(f"   • Total Profit: ₹{df_sales['profit'].sum():,.0f}")
print(f"   • Average Order Value: ₹{df_sales['revenue'].mean():,.0f}")

print("\n📁 FILES CREATED:")
print("   1. dim_product.csv")
print("   2. dim_customer.csv")
print("   3. dim_date.csv")
print("   4. fact_sales_monthly.csv")
print("   5. fact_targets.csv")

print("\n🎉 Ready for analysis! Import these into MySQL or Tableau.")
print("="*60 + "\n")
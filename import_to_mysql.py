#!/usr/bin/env python3
"""
Import CSV files to MySQL Database
"""

import pandas as pd
import mysql.connector
from mysql.connector import Error

print("\n" + "="*60)
print("   IMPORTING DATA TO MYSQL")
print("="*60 + "\n")

# Database connection
try:
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='atliq123',  # Use your MySQL password
        database='atliq_hardware'
    )
    
    if connection.is_connected():
        print("✅ Connected to MySQL database\n")
        cursor = connection.cursor()
        
        # 1. Import Products
        print("📦 Importing Products...")
        df_products = pd.read_csv('dim_product.csv')
        for _, row in df_products.iterrows():
            cursor.execute(
                "INSERT INTO dim_product VALUES (%s, %s, %s, %s, %s)",
                tuple(row)
            )
        print(f"   ✅ Imported {len(df_products)} products")
        
        # 2. Import Customers
        print("\n👥 Importing Customers...")
        df_customers = pd.read_csv('dim_customer.csv')
        for _, row in df_customers.iterrows():
            cursor.execute(
                "INSERT INTO dim_customer VALUES (%s, %s, %s, %s, %s, %s)",
                tuple(row)
            )
        print(f"   ✅ Imported {len(df_customers)} customers")
        
        # 3. Import Dates
        print("\n📅 Importing Dates...")
        df_dates = pd.read_csv('dim_date.csv')
        for _, row in df_dates.iterrows():
            cursor.execute(
                "INSERT INTO dim_date VALUES (%s, %s, %s, %s, %s, %s, %s)",
                tuple(row)
            )
        print(f"   ✅ Imported {len(df_dates)} dates")
        
        # 4. Import Sales
        print("\n💰 Importing Sales Transactions...")
        df_sales = pd.read_csv('fact_sales_monthly.csv')
        for _, row in df_sales.iterrows():
            cursor.execute(
                "INSERT INTO fact_sales_monthly VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
                tuple(row)
            )
        print(f"   ✅ Imported {len(df_sales)} transactions")
        
        # 5. Import Targets
        print("\n🎯 Importing Targets...")
        df_targets = pd.read_csv('fact_targets.csv')
        for _, row in df_targets.iterrows():
            cursor.execute(
                "INSERT INTO fact_targets (fiscal_year, month, month_name, department, target_revenue) VALUES (%s, %s, %s, %s, %s)",
                tuple(row)
            )
        print(f"   ✅ Imported {len(df_targets)} targets")
        
        # Commit all changes
        connection.commit()
        print("\n" + "="*60)
        print("   ✅ ALL DATA IMPORTED SUCCESSFULLY!")
        print("="*60 + "\n")
        
except Error as e:
    print(f"❌ Error: {e}")

finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("🔒 MySQL connection closed\n")


import sqlite3
import json

# Read JSON
with open(r"./files/lidl.json", "r", encoding="utf-8") as file:
    file_data = json.load(file)

# Create Database
conn = sqlite3.connect(r"sql_database.db")
cursor = conn.cursor()

# Create Table in SQLite
cursor.execute('''
    CREATE TABLE IF NOT EXISTS kaufda_offers (
        id TEXT,
        name TEXT,
        category TEXT,
        regular_price REAL,
        sales_price REAL
    )
''')

# Scraping
for page in file_data["contents"]: 
    for offer in page["offers"]: 
        content = offer["content"]
        id_number = content["id"]
        
        # Extract product information
        for product in content["products"]:
            product_name = product["name"]

            # Extract Category of the product 
            product_category = None
            if product.get("categoryPaths"):
                product_category = product["categoryPaths"][0]["name"]
            #else:
             #   product_category = "N/A"

            # Initialize prices for each product
            regular_price = None
            sales_price = None
            
            # Extract price information
            for price in content["deals"]:
                if price["type"] == "SALES_PRICE":
                    sales_price = price["min"]
                elif price["type"] == "REGULAR_PRICE":
                    regular_price = price["min"]

            # 
            cursor.execute('''
                INSERT INTO kaufda_offers (id, name, category, regular_price, sales_price)
                VALUES (?, ?, ?, ?, ?)
            ''', (id_number, product_name, product_category, regular_price, sales_price))

# Save changes and close
conn.commit()

# See data in Python environment
#cursor.execute("SELECT * FROM kaufda_offers")
#all_products = cursor.fetchall()

#for item in all_products:
    #print(f"id: {item[0]}, Name: {item[1]}, Category: {item[2]}, Regular Price: {item[3]}, Sales Price: {item[4]}")

conn.close();



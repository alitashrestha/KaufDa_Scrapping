# to find products less than 1 euro and product where you save more than 1 euro

import sqlite3
con = sqlite3.connect("sql_database.db")

cur = con.cursor()

res = cur.execute("SELECT * FROM kaufda_offers")
all_products = res.fetchall();

einEuroProducts =[]
savingMoreThan1 = []

for product in all_products:
    if product[4] is not None and product[4] < 1:
        einEuroProducts.append(product)

for product in einEuroProducts:
    print(f"Name: {product[1]}; Sales_Price: {product[4]}")
    
for product in all_products:
    regular_price = product[3]
    sales_price = product[4]
    if regular_price is not None and sales_price is not None:
        difference = regular_price - sales_price
        if difference > 1:
            print(f"Savings greater than 1! You save: {difference}")

con.close()



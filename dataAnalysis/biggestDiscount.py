# to find biggest discount

import sqlite3
from collections import defaultdict

con = sqlite3.connect("DB/all_data.db")

cur = con.cursor()

res = cur.execute("SELECT * FROM kaufda_offers")
all_products = res.fetchall();

# answering questions:
# 1. Biggest biggest_Discount
# 2. Highest average biggest_Discount
# 3. Where is your groceries shopping cheapest

# 1. Biggest biggest_Discount
biggest_Discount = {
  "name": None,
  "regular_price": 0,
  "sales_price": 0,
  "discount":0
}

for product in all_products:
    regular_price = product[3]
    sales_price = product[4]
    if regular_price is not None and sales_price is not None:
        difference = regular_price - sales_price
        if biggest_Discount['discount'] < difference:
            biggest_Discount={
                "name": product[1],
                "regular_price": regular_price,
                "sales_price": sales_price,
                "discount":difference
            }
print(f"Biggest Discount: {biggest_Discount}")

# 2.highest average discount

# Step A: Group all discounts by store
store_discounts = defaultdict(list)

for product in all_products:
    regular_price = product[3]
    sales_price = product[4]
    store_name = product[5] # 'store' is the 6th column (index 5)

    # Only calculate if we have valid prices
    if regular_price is not None and sales_price is not None:
        discount = regular_price - sales_price
        store_discounts[store_name].append(discount)

# Step B: Calculate averages and find the highest
best_store = None
highest_average = 0

for store, discounts in store_discounts.items():
    # Calculate average: Sum of discounts / Number of items
    if len(discounts) > 0:
        avg_discount = sum(discounts) / len(discounts)
        print(f"Store: {store}, Avg Discount: {avg_discount:.2f}")
        
        if avg_discount > highest_average:
            highest_average = avg_discount
            best_store = store

print(f"The store with the highest average discount is: {best_store} ({highest_average:.2f})")

# SQL Logic:
# 1. Calculate the total number of unique stores.
# 2. Group products by 'name'.
# 3. Keep only products where the number of unique stores they appear in 
#    matches the total number of stores.
query = """
    SELECT name, regular_price, sales_price
    FROM kaufda_offers 
    GROUP BY name 
    HAVING COUNT(DISTINCT store) = (SELECT COUNT(DISTINCT store) FROM kaufda_offers)
"""

cur.execute(query)
common_items = cur.fetchall()

print(f"Items found in ALL stores: {len(common_items)}")
for item in common_items:
    print(f"- {item}")


con.close()

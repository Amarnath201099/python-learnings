# Task 8: Inventory Management System
# Objective: Manage inventory using stacks, queues, and dictionaries.

from collections import deque

inventory = {
    "Laptop" : 10,
    "Keyboard" : 20,
    "Mouse" : 25,
    "Monitor": 10,
}

product_prices = [("Laptop", 1000), ("Keyboard", "400"), ("Mouse" , 200) , ("Monitor", 500)]

transactions = []

orders = deque()

def place_order(each_order):
    product, quantity = each_order
    if product not in inventory:
        return "Product doen't exist in inventory"
    if inventory[product] < quantity:
        return "Not enough stock"
    inventory[product] -= quantity
    transactions.append((product, quantity))
    return "Order Placed"


def undo_transaction(data):
    if not data:
        return "No transation to undo"
    product, quantity = data
    inventory[product] += quantity
    return "Return Successful"


orders.append(("Laptop", 2))
orders.append(("Keyboard", 4))
orders.append(("Mouse", 30))

index = 1

while orders:
    order = orders.popleft()
    order_status = place_order(order)
    print(f"Order {index} status: {order_status}")
    index += 1


print(undo_transaction(transactions.pop()))

print("Remaining Inventory: ")

for index, (product, quantity) in enumerate(inventory.items(), start=1):
    print(f"{index}. {product} : {quantity}")


print("Inventory Product Prices: ")

for each_inventory_product, each_product_price in zip(inventory, product_prices):
    if each_inventory_product == each_product_price[0]:
        print(f"{each_inventory_product} : {each_product_price[1]}Rs")



"""
==================== QUICK REVISION ====================

1. Dictionary (Inventory)
-------------------------------------------------------
- Stores data as key:value pairs.
- Access value: inventory["Laptop"]
- Loop with .items() to get both key and value.

Example:
for product, quantity in inventory.items():

-------------------------------------------------------

2. Queue (deque)
-------------------------------------------------------
- FIFO (First In, First Out)
- Add order  -> orders.append(order)
- Process    -> orders.popleft()

Use:
while orders:
    order = orders.popleft()

-------------------------------------------------------

3. Stack (List)
-------------------------------------------------------
- LIFO (Last In, First Out)
- Save transaction -> transactions.append(data)
- Undo latest      -> transactions.pop()

Always check before pop():
if transactions:

-------------------------------------------------------

4. enumerate()
-------------------------------------------------------
- Adds numbering while looping.

Example:
for index, (product, quantity) in enumerate(inventory.items(), start=1):

-------------------------------------------------------

5. zip()
-------------------------------------------------------
- Combines multiple iterables position by position.

Example:
zip(products, prices)

Returns:
("Laptop",1000)
("Mouse",200)

-------------------------------------------------------

6. Dictionary iteration mistake
-------------------------------------------------------
Wrong:
for item in inventory:
    item.key()

Reason:
- 'item' is just the key (string).

Correct:
for product, quantity in inventory.items():

-------------------------------------------------------

-------------------------------------------------------

7. Processing an order
-------------------------------------------------------
Check product exists
        ↓
Check stock available
        ↓
Reduce inventory
        ↓
Save transaction (stack)
        ↓
Order processed

=======================================================
"""
"""
Project
You are tasked with creating a simple inventory management system for a market. The system should
allow users to add, update, view, and remove items from the inventory. Each item in the inventory
will have a name, price, quantity, and category.

Functionality:

Add Item: Create a function add_item that allows users to add a new item to the inventory.
Users should input the name, price, quantity, and category of the item.

Update Item: Implement a function update_item that allows users to update the details of an
existing item in the inventory. Users should be able to update the price, quantity, and
category of the item.

View Inventory: Develop a function view_inventory that displays all items in the inventory along
with their details (name, price, quantity, and category).

Remove Item: Create a function remove_item that allows users to remove an item from the inventory
based on its name.

Search by Category: Implement a function search_by_category that allows users to search for items
in the inventory based on their category. The function should display all items belonging to the
specified category.

Project Structure:
Define a list inventory to store the items in the market inventory. Each item should be represented
as a dictionary with keys for name, price, quantity, and category.

Implement the functions add_item, update_item, view_inventory, remove_item, and search_by_category
to manage the inventory.

Create a main loop to interact with the user. The loop should prompt the user to choose from various
options such as adding, updating, viewing, removing items, or searching by category.
"""

def add_item():
    str_name= input("Enter item name: ")
    for item in items:
        if item["name"] == str_name.upper():
            print(item["name"], "already in inventory.")
            return
    flt_price= input("Enter price: ")
    int_quant= input("Enter quantity: ")
    str_cat= input("Enter category: ")
    item = {
        "name": str_name.upper(),
        "price": float(flt_price),
        "quantity": int(int_quant),
        "category": str_cat.upper()
    }
    items.append(item)
    print("Item '", item["name"], "' added successfully.", sep="")

    return

def view_inventory():
    print("Current Inventory")
    print("------------------------------")
    if not items:
        print("Currently no inventory in database.")
    else:
        for item in items:
            print("Product: ",item["name"])
            print("Price: ", item["price"])
            print("Number left: ", item["quantity"])
            print("Category: ", item["category"])
            print("------------------------------")
    return

def update_item():
    print("Sell-Product Menu")
    str_product=input("Enter name of product sold: ")
    bool_found = False
    for item in items:
        if item["name"] == str_product.upper():
            bool_found = True
            print("We have",item["quantity"], "of", item["name"])
            int_sold=int(input("Enter quantity to sell: "))
            item["quantity"] -= int_sold
            print("There are now",item["quantity"], "of", item["name"], "remaining.")
            if item["quantity"] < 0:
                print("WARNING: System shows more sold than were on shelf!")
    if not bool_found:
        print("Item", str_product.upper(),"not found. Check your spelling.")
    return

def remove_item():
    str_product=input("Enter name of product to delete: ")
    for item in items:
        if item["name"] == str_product.upper():
            if item["quantity"] > 0:
                print("We have",item["quantity"], "of", item["name"])
                print("Cannot remove from database while product remains on shelf!")
                return
            print("Removing", item["name"], "from database. If you are sure, type YES :")
            str_input = input()
            if str_input.upper() == "YES":
                items.remove(item)
                print (str_product.upper(), "has been removed from database.")
            else:
                print ("Removal cancelled.")
            return
    print("Item", str_product.upper(), "not found. Check your spelling.")
    return

def category_search():
    str_category=input("Enter name of category to display: ")
    print("Showing all products in category", str_category.upper())
    print("------------------------------")
    bool_found=False
    for item in items:
        if item["category"] == str_category.upper():
            bool_found = True
            print("Product: ",item["name"])
            print("Price: ", item["price"])
            print("Number left: ", item["quantity"])
            print("------------------------------")
    if not bool_found:
        print("No products found in category",str_category.upper())
    return

items=[]

intMenu = 0
while intMenu != 6:
    print("Inventory Management System")
    print("1. Add Item")
    print("2. Sell Items")
    print("3. View Inventory")
    print("4. Remove Item")
    print("5. Search by Category")
    print("6. Exit")
    strMenu = input("Choose an option (1-6): ")
    intMenu = 0
    if strMenu.isdigit():
        intMenu=int(strMenu)
    if intMenu == 1:
        add_item()
    if intMenu == 2:
        update_item()
    if intMenu == 3:
        view_inventory()
    if intMenu == 4:
        remove_item()
    if intMenu == 5:
        category_search()

print("Exiting program.")
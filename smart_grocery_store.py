# ==========================================
# SMART GROCERY STORE MANAGEMENT SYSTEM
# ==========================================

# List of dictionaries to store products
products = [
    {"id": 101, "name": "Milk", "category": "Dairy", "price": 250, "stock": 20},
    {"id": 102, "name": "Bread", "category": "Bakery", "price": 150, "stock": 15},
    {"id": 103, "name": "Rice", "category": "Grocery", "price": 300, "stock": 10},
    {"id": 104, "name": "Eggs", "category": "Dairy", "price": 30, "stock": 25},
    {"id": 105, "name": "Sugar", "category": "Grocery", "price": 180, "stock": 4}
]

# Separate list to store completed sales
sales = []


# Find a product using its ID
def find_product(product_id):
    for product in products:
        if product["id"] == product_id:
            return product
    return None


# Display all available products
def display_products():
    print("\n========== ALL PRODUCTS ==========")

    if not products:
        print("No products available.")
        return

    for product in products:
        print("---------------------------------")
        print("Product ID:", product["id"])
        print("Name:", product["name"])
        print("Category:", product["category"])
        print("Price: Rs.", product["price"])
        print("Available Stock:", product["stock"])


# Add a new product to the products list
def add_product():
    print("\n========== ADD NEW PRODUCT ==========")

    try:
        product_id = int(input("Enter Product ID: "))

        # Prevent duplicate product IDs
        if find_product(product_id) is not None:
            print("Error: Product ID already exists!")
            return

        name = input("Enter Product Name: ").strip()
        category = input("Enter Category: ").strip()
        price = float(input("Enter Product Price: "))
        stock = int(input("Enter Available Stock: "))

        # Validate product information
        if product_id <= 0 or not name or not category or price <= 0 or stock < 0:
            print("Invalid product information!")
            return

        # Create a dictionary for the new product
        new_product = {
            "id": product_id,
            "name": name,
            "category": category,
            "price": price,
            "stock": stock
        }

        # Add the dictionary to the products list
        products.append(new_product)
        print("Product added successfully!")

    except ValueError:
        print("Invalid input! Please enter correct numeric values.")


# Search for a product by name or ID
def search_product():
    print("\n========== SEARCH PRODUCT ==========")
    search_value = input("Enter Product Name or ID: ").strip()

    for product in products:
        if (search_value.lower() == product["name"].lower()
                or search_value == str(product["id"])):
            print("\nProduct Found!")
            print("Product ID:", product["id"])
            print("Name:", product["name"])
            print("Category:", product["category"])
            print("Price: Rs.", product["price"])
            print("Available Stock:", product["stock"])
            return

    print("Product not found!")


# Add stock or set a new stock quantity
def update_stock():
    print("\n========== UPDATE PRODUCT STOCK ==========")

    try:
        product_id = int(input("Enter Product ID: "))
        product = find_product(product_id)

        if product is None:
            print("Product not found!")
            return

        print("Current Stock:", product["stock"])
        print("1. Add Stock")
        print("2. Set New Stock Quantity")
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            quantity = int(input("Enter quantity to add: "))
            if quantity <= 0:
                print("Quantity must be greater than zero!")
                return
            product["stock"] += quantity

        elif choice == "2":
            quantity = int(input("Enter new stock quantity: "))
            if quantity < 0:
                print("Stock cannot be negative!")
                return
            product["stock"] = quantity

        else:
            print("Invalid choice!")
            return

        print("Stock updated successfully!")
        print("New Available Stock:", product["stock"])

    except ValueError:
        print("Please enter valid numeric values!")


# Process a customer purchase and save the sale record
def process_sale():
    print("\n========== PROCESS CUSTOMER SALE ==========")

    try:
        product_id = int(input("Enter Product ID: "))
        product = find_product(product_id)

        if product is None:
            print("Product not found!")
            return

        quantity = int(input("Enter Purchase Quantity: "))

        if quantity <= 0:
            print("Quantity must be greater than zero!")
            return

        # Check that enough stock is available
        if quantity > product["stock"]:
            print("Insufficient stock!")
            print("Available Stock:", product["stock"])
            return

        # Calculate the total price and update stock
        total_amount = product["price"] * quantity
        product["stock"] -= quantity

        # Create and save the sales dictionary
        sale_record = {
            "product_id": product["id"],
            "product_name": product["name"],
            "quantity_sold": quantity,
            "total_amount": total_amount
        }
        sales.append(sale_record)

        # Display purchase summary
        print("\n========== PURCHASE SUMMARY ==========")
        print("Product:", product["name"])
        print("Quantity Sold:", quantity)
        print("Price Per Unit: Rs.", product["price"])
        print("Total Amount: Rs.", total_amount)
        print("Remaining Stock:", product["stock"])
        print("Sale completed successfully!")

    except ValueError:
        print("Invalid input! Enter numeric values.")


# Display all completed sales
def view_sales():
    print("\n========== SALES RECORDS ==========")

    if not sales:
        print("No sales records available.")
        return

    for sale in sales:
        print("---------------------------------")
        print("Product ID:", sale["product_id"])
        print("Product Name:", sale["product_name"])
        print("Quantity Sold:", sale["quantity_sold"])
        print("Total Amount: Rs.", sale["total_amount"])


# Generate a summary report for the store
def generate_report():
    print("\n========== STORE REPORT ==========")

    total_products = len(products)

    # Calculate total available stock
    total_stock = 0
    for product in products:
        total_stock += product["stock"]

    # Calculate total sales transactions and revenue
    total_transactions = len(sales)
    total_revenue = 0
    for sale in sales:
        total_revenue += sale["total_amount"]

    print("Total Products:", total_products)
    print("Total Available Stock:", total_stock)
    print("Total Sales Transactions:", total_transactions)
    print("Total Revenue: Rs.", total_revenue)

    # Display products with fewer than 5 units in stock
    print("\nProducts with Stock Below 5:")
    low_stock_found = False

    for product in products:
        if product["stock"] < 5:
            print(product["name"], "-", product["stock"], "units")
            low_stock_found = True

    if not low_stock_found:
        print("No low-stock products.")

    # Find the highest- and lowest-priced products
    if products:
        highest_price = max(products, key=lambda item: item["price"])
        lowest_price = min(products, key=lambda item: item["price"])

        print("\nHighest Priced Product:")
        print(highest_price["name"], "- Rs.", highest_price["price"])

        print("\nLowest Priced Product:")
        print(lowest_price["name"], "- Rs.", lowest_price["price"])


# ==========================================
# MAIN MENU
# ==========================================

while True:
    print("\n====================================")
    print("   SMART GROCERY STORE SYSTEM")
    print("====================================")
    print("1. Add New Product")
    print("2. View All Products")
    print("3. Search Product")
    print("4. Update Product Stock")
    print("5. Process Customer Sale")
    print("6. View Sales Records")
    print("7. Generate Store Report")
    print("8. Exit")

    choice = input("\nEnter your choice: ").strip()

    if choice == "1":
        add_product()
    elif choice == "2":
        display_products()
    elif choice == "3":
        search_product()
    elif choice == "4":
        update_stock()
    elif choice == "5":
        process_sale()
    elif choice == "6":
        view_sales()
    elif choice == "7":
        generate_report()
    elif choice == "8":
        print("Thank you for using Smart Grocery Store System!")
        break
    else:
        print("Invalid choice! Please select between 1 and 8.")

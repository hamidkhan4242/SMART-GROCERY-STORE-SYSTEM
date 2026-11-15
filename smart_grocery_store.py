# ==========================================
# SMART GROCERY STORE MANAGEMENT SYSTEM
# ==========================================

import io
import math
import sys
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch

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

        # Reject NaN and infinity (float() accepts "nan", "inf", "1e999")
        if not math.isfinite(price):
            print("Invalid price! Price must be a finite number.")
            return

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

def main():
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


# ==========================================
# AUTOMATIC TESTS
# Run with:  python smart_grocery_store.py test
# ==========================================

SAMPLE = [
    {"id": 101, "name": "Milk", "category": "Dairy", "price": 250, "stock": 20},
    {"id": 102, "name": "Bread", "category": "Bakery", "price": 150, "stock": 15},
    {"id": 103, "name": "Rice", "category": "Grocery", "price": 300, "stock": 10},
    {"id": 104, "name": "Eggs", "category": "Dairy", "price": 30, "stock": 25},
    {"id": 105, "name": "Sugar", "category": "Grocery", "price": 180, "stock": 4},
]


def run(func, *inputs):
    """Run a store function with fake user inputs and return what it printed."""
    out = io.StringIO()
    with patch("builtins.input", side_effect=list(inputs)), redirect_stdout(out):
        func()
    return out.getvalue()


class StoreTestCase(unittest.TestCase):
    def setUp(self):
        products[:] = [dict(p) for p in SAMPLE]
        sales.clear()


class TestAddProduct(StoreTestCase):
    def test_valid_product_is_added(self):
        out = run(add_product, "200", "Tea", "Grocery", "500", "10")
        self.assertIn("Product added successfully", out)
        self.assertEqual(len(products), 6)

    def test_duplicate_id_rejected(self):
        out = run(add_product, "101")
        self.assertIn("already exists", out)
        self.assertEqual(len(products), 5)

    def test_nan_price_rejected(self):
        for bad in ("nan", "NaN", "-nan"):
            with self.subTest(price=bad):
                out = run(add_product, "200", "Tea", "Grocery", bad, "10")
                self.assertIn("finite", out)
                self.assertIsNone(find_product(200))

    def test_infinite_price_rejected(self):
        for bad in ("inf", "-inf", "Infinity", "1e999"):
            with self.subTest(price=bad):
                out = run(add_product, "200", "Tea", "Grocery", bad, "10")
                self.assertIn("finite", out)
                self.assertIsNone(find_product(200))

    def test_zero_and_negative_price_rejected(self):
        for bad in ("0", "-5"):
            with self.subTest(price=bad):
                out = run(add_product, "200", "Tea", "Grocery", bad, "10")
                self.assertIn("Invalid product information", out)
                self.assertIsNone(find_product(200))

    def test_negative_stock_rejected(self):
        out = run(add_product, "200", "Tea", "Grocery", "50", "-1")
        self.assertIn("Invalid product information", out)

    def test_zero_stock_allowed(self):
        run(add_product, "200", "Tea", "Grocery", "50", "0")
        self.assertEqual(find_product(200)["stock"], 0)

    def test_empty_name_or_category_rejected(self):
        out = run(add_product, "200", "   ", "Grocery", "50", "5")
        self.assertIn("Invalid product information", out)
        out = run(add_product, "201", "Tea", "", "50", "5")
        self.assertIn("Invalid product information", out)

    def test_zero_or_negative_id_rejected(self):
        for bad in ("0", "-7"):
            with self.subTest(id=bad):
                out = run(add_product, bad, "Tea", "Grocery", "50", "5")
                self.assertIn("Invalid product information", out)

    def test_non_numeric_input_rejected(self):
        out = run(add_product, "abc")
        self.assertIn("Invalid input", out)
        out = run(add_product, "200", "Tea", "Grocery", "abc", "5")
        self.assertIn("Invalid input", out)
        out = run(add_product, "200", "Tea", "Grocery", "50", "2.5")
        self.assertIn("Invalid input", out)
        self.assertEqual(len(products), 5)


class TestSearchAndView(StoreTestCase):
    def test_search_by_id(self):
        self.assertIn("Product Found", run(search_product, "103"))

    def test_search_by_name_case_insensitive(self):
        self.assertIn("Product Found", run(search_product, "  mIlK "))

    def test_search_not_found(self):
        self.assertIn("Product not found", run(search_product, "Soap"))

    def test_view_with_no_products(self):
        products.clear()
        self.assertIn("No products available", run(display_products))


class TestUpdateStock(StoreTestCase):
    def test_add_stock(self):
        run(update_stock, "101", "1", "5")
        self.assertEqual(find_product(101)["stock"], 25)

    def test_set_stock_to_zero(self):
        run(update_stock, "101", "2", "0")
        self.assertEqual(find_product(101)["stock"], 0)

    def test_negative_stock_rejected(self):
        out = run(update_stock, "101", "2", "-3")
        self.assertIn("cannot be negative", out)
        self.assertEqual(find_product(101)["stock"], 20)

    def test_add_zero_or_negative_rejected(self):
        for bad in ("0", "-4"):
            with self.subTest(qty=bad):
                out = run(update_stock, "101", "1", bad)
                self.assertIn("greater than zero", out)
                self.assertEqual(find_product(101)["stock"], 20)

    def test_unknown_product_and_bad_choice(self):
        self.assertIn("Product not found", run(update_stock, "999"))
        self.assertIn("Invalid choice", run(update_stock, "101", "9"))

    def test_non_numeric_input(self):
        self.assertIn("valid numeric", run(update_stock, "abc"))


class TestProcessSale(StoreTestCase):
    def test_valid_sale(self):
        out = run(process_sale, "101", "2")
        self.assertIn("Sale completed successfully", out)
        self.assertEqual(find_product(101)["stock"], 18)
        self.assertEqual(sales[0]["total_amount"], 500)

    def test_sell_exact_remaining_stock(self):
        run(process_sale, "105", "4")
        self.assertEqual(find_product(105)["stock"], 0)
        self.assertEqual(len(sales), 1)

    def test_insufficient_stock_no_sale(self):
        out = run(process_sale, "105", "5")
        self.assertIn("Insufficient stock", out)
        self.assertEqual(find_product(105)["stock"], 4)
        self.assertEqual(sales, [])

    def test_zero_and_negative_quantity(self):
        for bad in ("0", "-2"):
            with self.subTest(qty=bad):
                out = run(process_sale, "101", bad)
                self.assertIn("greater than zero", out)
                self.assertEqual(sales, [])

    def test_unknown_product(self):
        self.assertIn("Product not found", run(process_sale, "999"))

    def test_non_numeric_input(self):
        self.assertIn("Invalid input", run(process_sale, "101", "two"))
        self.assertEqual(sales, [])

    def test_sold_out_product_cannot_be_sold_again(self):
        run(process_sale, "105", "4")
        out = run(process_sale, "105", "1")
        self.assertIn("Insufficient stock", out)


class TestSalesAndReport(StoreTestCase):
    def test_view_sales_empty(self):
        self.assertIn("No sales records", run(view_sales))

    def test_view_sales_lists_sale(self):
        run(process_sale, "104", "3")
        self.assertIn("Eggs", run(view_sales))

    def test_report_totals(self):
        run(process_sale, "101", "2")   # 500
        run(process_sale, "104", "10")  # 300
        out = run(generate_report)
        self.assertIn("Total Products: 5", out)
        self.assertIn("Total Available Stock: 62", out)  # 74 - 12 sold = 62
        self.assertIn("Total Sales Transactions: 2", out)
        self.assertIn("Total Revenue: Rs. 800", out)

    def test_report_low_stock_below_five_only(self):
        out = run(generate_report)
        self.assertIn("Sugar - 4 units", out)
        find_product(105)["stock"] = 5  # exactly 5 is NOT low stock
        out = run(generate_report)
        self.assertIn("No low-stock products", out)

    def test_report_highest_and_lowest_price(self):
        out = run(generate_report)
        self.assertIn("Rice - Rs. 300", out)
        self.assertIn("Eggs - Rs. 30", out)

    def test_report_with_no_products(self):
        products.clear()
        out = run(generate_report)
        self.assertIn("Total Products: 0", out)
        self.assertNotIn("Highest Priced", out)


class TestMenu(StoreTestCase):
    def test_invalid_menu_choice_then_exit(self):
        out = run(main, "99", "", "abc", "8")
        self.assertIn("Invalid choice", out)
        self.assertIn("Thank you", out)

    def test_menu_runs_options_then_exits(self):
        out = run(main, "2", "7", "8")
        self.assertIn("ALL PRODUCTS", out)
        self.assertIn("STORE REPORT", out)


# ==========================================
# START THE PROGRAM
# ==========================================

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "test":
        # Run the tests instead of the menu
        unittest.main(argv=["smart_grocery_store"], verbosity=2)
    else:
        main()

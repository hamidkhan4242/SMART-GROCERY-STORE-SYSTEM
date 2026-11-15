# Smart Grocery Store Management System

## Project Overview

The **Smart Grocery Store Management System** is a beginner-friendly,
menu-driven Python application for managing a local grocery store. It
helps the store owner maintain product details, manage stock, process
customer sales, view sales records, and generate a store report.

The project uses Python lists and dictionaries to store information in
memory while the program is running.

## Features

1.  **Add New Product**
    -   Enter a product ID, name, category, price, and available stock.
    -   Prevent duplicate product IDs.
    -   Reject invalid prices, including zero, negative, `NaN`, and
        infinite values (`inf`, `-inf`, `1e999`).
    -   Store each product as a dictionary in the products list.
2.  **View All Products**
    -   Display all products with their IDs, names, categories, prices,
        and stock quantities.
3.  **Search Product**
    -   Search for a product by its name or ID.
    -   Display complete details when a match is found.
4.  **Update Product Stock**
    -   Find a product using its ID.
    -   Add more stock or set a new stock quantity.
5.  **Process Customer Sale**
    -   Enter a product ID and purchase quantity.
    -   Check that the product exists and enough stock is available.
    -   Calculate the total price, deduct the sold quantity, and save
        the sale.
6.  **View Sales Records**
    -   Display completed sales, including product ID, product name,
        quantity sold, and total amount.
7.  **Generate Store Report**
    -   Show the total number of products.
    -   Calculate total available stock.
    -   Count sales transactions and calculate total revenue.
    -   List products with fewer than 5 units in stock.
    -   Identify the highest-priced and lowest-priced products.
8.  **Exit**
    -   Close the application.

## Project Structure

``` text
smart-grocery-store/
│
├── smart_grocery_store.py   (program + automatic tests)
└── README.md
```

## Python Concepts and Techniques Used

-   **Lists:** Store multiple product and sales records.
-   **Dictionaries:** Store each product and sale as key-value pairs.
-   **List `append()` method:** Add new products and completed sales.
-   **Functions:** Organize the application into reusable tasks.
-   **`for` loops:** Search, display, and calculate information from
    records.
-   **`while` loop:** Keep the menu running until the user exits.
-   **Conditional statements:** Handle menu choices, product searches,
    and stock checks.
-   **Dictionary keys:** Access product and sales information.
-   **Input validation:** Use `try-except` to handle invalid numeric
    input and checks to prevent invalid prices, quantities, and
    duplicate IDs.
-   **Built-in functions:** Use `len()`, `max()`, and `min()` in the
    store report.
-   **`math.isfinite()`:** Reject `NaN` and infinite prices.
-   **`unittest` and `unittest.mock`:** Test the program automatically
    without typing inputs by hand.

## Requirements

-   Python 3.x
-   No external Python libraries are required.

## How to Run the Program

1.  Install Python 3 if it is not already installed.
2.  Save the program as `smart_grocery_store.py`.
3.  Open a terminal in the folder containing the file.
4.  Run:

``` bash
python smart_grocery_store.py
```

On some systems, use:

``` bash
python3 smart_grocery_store.py
```

5.  Select an option from the menu by entering a number from `1` to `8`.

## Running the Tests

The tests are written inside `smart_grocery_store.py` itself (at the
bottom of the file), so no extra file is needed. To run the tests instead
of the menu, use:

``` bash
python smart_grocery_store.py test
```

(or `python3 smart_grocery_store.py test` on some systems). Running the
program without the word `test` starts the normal menu.

## Test Results

**Result: 35 tests run, 35 passed, 0 failed (`OK`).**

| Area                | What is tested                                                                                                                         | Tests |
|---------------------|----------------------------------------------------------------------------------------------------------------------------------------|------:|
| Add Product         | Valid product, duplicate ID, `NaN` price (`nan`, `NaN`, `-nan`), infinite price (`inf`, `-inf`, `Infinity`, `1e999`), zero/negative price, negative stock, zero stock allowed, empty name/category, zero/negative ID, non-numeric and decimal input | 10 |
| Search / View       | Search by ID, by name (case-insensitive, extra spaces), not found, view with no products                                               | 4 |
| Update Stock        | Add stock, set stock to 0, negative stock rejected, add 0/negative rejected, unknown product, invalid choice, non-numeric input       | 6 |
| Process Sale        | Valid sale, selling exact remaining stock, insufficient stock, zero/negative quantity, unknown product, non-numeric input, sold-out item | 7 |
| Sales and Report    | Empty sales list, sales listing, totals and revenue, low stock (below 5 only, exactly 5 is not low), highest/lowest price, report with no products | 6 |
| Menu                | Invalid menu choice then exit, running options then exit                                                                               | 2 |

Output of the run:

``` text
Ran 35 tests in 0.008s

OK
```

### Bug found and fixed

Python's `float()` accepts the text `nan` and `inf`. Because every
comparison with `NaN` is `False`, the original check `price <= 0` did
not reject it, and a product with price `nan` was saved. The program now
checks `math.isfinite(price)` and shows:
`Invalid price! Price must be a finite number.`

### Changes made for testing

The menu loop was moved into a `main()` function. At the bottom of the
file, `if __name__ == "__main__":` decides what to run: the tests when
`test` is given, otherwise the normal menu. The program works exactly the
same way as before.

## Sample Data

The application starts with these example products:

    Product ID Product Name   Category     Price (Rs.)   Stock
  ------------ -------------- ---------- ------------- -------
           101 Milk           Dairy                250      20
           102 Bread          Bakery               150      15
           103 Rice           Grocery              300      10
           104 Eggs           Dairy                 30      25
           105 Sugar          Grocery              180       4

## Sample Execution

Example of processing a sale:

``` text
Enter your choice: 5

Enter Product ID: 101
Enter Purchase Quantity: 2

========== PURCHASE SUMMARY ==========
Product: Milk
Quantity Sold: 2
Price Per Unit: Rs. 250
Total Amount: Rs. 500
Remaining Stock: 18
Sale completed successfully!
```

The sale is added to the sales list, and the product's available stock
is reduced by the purchased quantity.

## Important Notes

-   Product and sales data are stored in Python lists, so they are
    available only while the program is running.
-   Data is not permanently saved to a file or database.
-   A sale is recorded only when the product exists and sufficient stock
    is available.
-   Product stock cannot be set to a negative quantity.
-   Products with stock below 5 units appear in the low-stock section of
    the report.

## Author

**Student Name:** \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

**Roll Number:** \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

**Course / Class:** \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

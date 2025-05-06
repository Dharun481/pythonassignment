# entry_display.py
products = []
prices = []
quantities = []

def add_product():
    product = input("Enter a Product Name (or 'q' to quit): ")
    if product.lower() == "q":
        return False
    price = float(input(f"Enter the price of {product}: ₹"))
    quantity = int(input(f"Enter the quantity of {product}: "))
    products.append(product)
    prices.append(price)
    quantities.append(quantity)
    print(f"{product} added successfully!\n")
    return True

def display_product():
    print("\n---- Product List ----")
    for i in range(len(products)):
        print(f"{products[i]} : ₹{prices[i]} (Qty: {quantities[i]})")
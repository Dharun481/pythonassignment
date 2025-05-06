# update_delete.py
import entry_display

def update_product():
    product_name = input("Enter the product name to update: ")
    if product_name in entry_display.products:
        index = entry_display.products.index(product_name)
        new_price = float(input(f"Enter new price for {product_name}: ₹"))
        new_quantity = int(input(f"Enter new quantity for {product_name}: "))
        entry_display.prices[index] = new_price
        entry_display.quantities[index] = new_quantity
        print(f"\n{product_name} updated successfully!\n")
    else:
        print(f"\nProduct not found. Adding it as a new product...\n")
        new_price = float(input(f"Enter price for new product {product_name}: ₹"))
        new_quantity = int(input(f"Enter quantity for new product {product_name}: "))
        entry_display.products.append(product_name)
        entry_display.prices.append(new_price)
        entry_display.quantities.append(new_quantity)
        print(f"{product_name} added successfully!\n")

def delete_product():
    product_name = input("Enter the product name to delete: ")
    if product_name in entry_display.products:
        index = entry_display.products.index(product_name)
        entry_display.products.pop(index)
        entry_display.prices.pop(index)
        entry_display.quantities.pop(index)
        print(f"{product_name} deleted successfully!\n")
    else:
        print(f"\nProduct '{product_name}' not found!\n")

# purchase.py
import entry_display

def purchase():
    cart = []
    total = 0

    print("\n---- Available Products ----")
    entry_display.display_product()

    while True:
        product = input("\nEnter the product to buy (or 'done' to finish): ")
        if product.lower() == 'done':
            break
        if product in entry_display.products:
            index = entry_display.products.index(product)
            max_qty = entry_display.quantities[index]
            if max_qty == 0:
                print("Out of stock!")
                continue
            quantity = int(input(f"Enter quantity for {product} (Available: {max_qty}): "))
            if quantity > max_qty:
                print("Not enough stock available.")
                continue
            price = entry_display.prices[index]
            cost = price * quantity
            total += cost
            cart.append((product, price, quantity, cost))
            entry_display.quantities[index] -= quantity
        else:
            print("Product not found!")

    if not cart:
        print("\nNo items purchased.")
        return

    discount = 0
    if total > 1000:
        discount = 0.10 * total
    tax = 0.18 * (total - discount)
    final_amount = total - discount + tax

    
    print("\n---- BILL ----")
    print("Product     Price   Qty   Cost")
    print("------------------------------")
    for item in cart:
        print(f"{item[0]}    {item[1]:.2f}   {item[2]}   {item[3]:.2f}")
    print("------------------------------")
    print(f"Total: {total:.2f}")
    print(f"Discount: -{discount:.2f}")
    print(f"Tax (18%): +{tax:.2f}")
    print(f"Final Amount: {final_amount:.2f}")
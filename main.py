# main.py
import entry_display
import update_delete
import purchase

def main_menu():
    while True:
        print("\n=== PRODUCT MANAGEMENT SYSTEM ===")
        print("1. Add Product")
        print("2. Display Products")
        print("3. Update Product")
        print("4. Delete Product")
        print("5. Purchase")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            while True:
                if not entry_display.add_product():
                    break
        elif choice == "2":
            entry_display.display_product()
        elif choice == "3":
            update_delete.update_product()
        elif choice == "4":
            update_delete.delete_product()
        elif choice == "5":
            purchase.purchase()
        elif choice == "6":
            print("Thank you for using the system!")
            break
        else:
            print("Invalid choice! Try again.")

main_menu()
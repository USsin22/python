
from product import Product
from inventory import Inventory


def main():
    inventory = Inventory()
    default_products = [
        Product("Laptop", 1200.00, 10),
        Product("Mouse", 25.50, 50),
        Product("Keyboard", 45.00, 30)
    ]
    for prod in default_products:
        inventory.add_product(prod)

    while True:
        print("\n----Inventory Menu ---")
        print("1. Add product")
        print("2. View products")
        print("3. Update stock")
        print("4. Exit")

        choice = input("Choose an option (1-4): ").strip()

        if choice == "1":
            name = input("Product name: ")
            price = float(input("Product price: "))
            stock = int(input("Initial stock: "))
            inventory.add_product(Product(name, price, stock))

        elif choice == "2":
            inventory.view_products()

        elif choice == "3":
            name = input("Product name to update: ")
            amount = int(input("Amount to add/remove (+/-): "))
            inventory.update_stock(name, amount)
            
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()

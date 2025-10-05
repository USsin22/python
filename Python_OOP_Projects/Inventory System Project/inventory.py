
class Inventory:
    def __init__(self):
        self.products = []
    def add_product(self, product):

        self.products.append(product)
        print(f"Added: { product}")

    def view_products(self):

        if not self.products:
            print("No  products in inventory.")
        for product in self.products:
            print(product)

    def update_stock(self, name, amount):
        for product in self.products:
            if product.name == name:
                product.stock += amount
                print(f"Updated {product.name}: {product.stock} in stock")
                return
        print("Product not found. ")

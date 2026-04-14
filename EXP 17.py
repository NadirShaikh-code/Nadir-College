#Name - Nadir Shaikh
#UIN - 251P086
print("Nadir Shaikh")
print("251P086")

class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock
    def update_stock(self, quantity):
        self.stock -= quantity

# Customer Class
class Customer:
    def __init__(self, name):
        self.name = name

# Shopping Cart Class
class ShoppingCart:
    def __init__(self):
        self.items = []
    # Add item to cart
    def add_item(self, product, quantity):
        if product.stock >= quantity:
            self.items.append((product, quantity))
            product.update_stock(quantity)
            print(f"{quantity} {product.name} added to cart")
        else:
            print(f"Not enough stock for {product.name}")
    # Calculate total cost
    def calculate_total(self):
        total = 0
        for product, quantity in self.items:
            total += product.price * quantity
        return total
    # Process order
    def checkout(self):
        total = self.calculate_total()
        print("\nOrder Summary:")
        for product, quantity in self.items:
            print(f"{product.name} x {quantity}")
        print("Total Amount:", total)
        print("Order Placed Successfully!")
# ----------- Main Program -----------
# Create products
p1 = Product("Laptop", 50000, 5)
p2 = Product("Mouse", 500, 10)
# Create customer
c1 = Customer("Mansi")
# Create cart
cart = ShoppingCart()
# Add items
cart.add_item(p1, 1)
cart.add_item(p2, 2)
# Checkout
cart.checkout()


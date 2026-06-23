class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def total_value(self):
        return self.price * self.quantity


product_data = [
    ("Laptop", 50000, 2),
    ("Mouse", 500, 10),
    ("Keyboard", 1500, 5)
]

products = []

for name, price, quantity in product_data:
    product = Product(name, price, quantity)
    products.append(product)

grand_total = 0

print("Inventory Details:")
for product in products:
    value = product.total_value()
    grand_total += value

    print(f"Product: {product.name}")
    print(f"Price: ₹{product.price}")
    print(f"Quantity: {product.quantity}")
    print(f"Total Value: ₹{value}")         
    print("-" * 30)

print(f"Grand Total Value of Inventory: ₹{grand_total}")
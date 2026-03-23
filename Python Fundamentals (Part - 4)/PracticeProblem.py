class Product:
    count = 0

    def __init__(self, name, price):
        self.name = name
        self.price = price
        Product.count += 1
    
    def get_info(self):  # Instance Method
        print(f"Name of the product is {self.name} and price is {self.price}")

    @classmethod
    def get_count(cls):
        print(f"Total products in store {cls.count}")

    @staticmethod
    def calc_discount(price, discount):
        print(f"discounted price = {price - (price * discount / 100)}")

p1 = Product("Phone", 10_000)
p2 = Product("Laptop", 50_000)
p3 = Product("Pen", 10)

p1.get_info()
p2.get_info()
p3.get_info()

Product.get_count()

p1.calc_discount(p1.price, 12)
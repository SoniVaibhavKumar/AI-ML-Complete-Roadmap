class Laptop:
    storage_type = "ssd"

    def __init__(self, RAM, storage):
        self.RAM = RAM
        self.storage = storage

    @classmethod
    def get_storage_type(cls):
        print(f"Storage type = {cls.storage_type}")
    
    def get_info(self):     # Instance method
        print(f"Laptop has {self.RAM} RAM and {self.storage} Storage with {self.storage_type} storage type")

    @staticmethod
    def calc_discount(price, discount):
        final_price = price - (discount * price / 100)
        print(f"discounted price = {final_price}")

l1 = Laptop("16gb", "512gb")
l2 = Laptop("8gb", "256gb")
l1.get_info()
l1.get_storage_type

l1.calc_discount(40_000, 10)
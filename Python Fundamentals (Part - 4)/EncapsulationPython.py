class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance

    def get_balance(self):  #getter
        return self.__balance()
    
    def set_balance(self, newBalance):
        self.__balance = newBalance

acc1 = BankAccount("Rahul Kumar", 100_000)
print(acc1.name, acc1._BankAccount__balance)
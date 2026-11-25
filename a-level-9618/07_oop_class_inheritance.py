"""OOP: classes, encapsulation and inheritance

Notes, live tools and self-marking practice:
https://revisionhub.online/a-level-computer-science-9618/further-programming/

Part of Revision Hub CS code examples - https://revisionhub.online
"""

class Account:
    def __init__(self, owner, balance=0):
        self.__owner = owner         # private attributes (encapsulation)
        self.__balance = balance

    def get_balance(self):
        return self.__balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def describe(self):
        return f"{self.__owner}: {self.__balance}"


class SavingsAccount(Account):      # inheritance
    def __init__(self, owner, balance, rate):
        super().__init__(owner, balance)
        self.__rate = rate

    def add_interest(self):
        self.deposit(self.get_balance() * self.__rate)

    def describe(self):              # polymorphism (overriding)
        return "Savings - " + super().describe()


if __name__ == "__main__":
    s = SavingsAccount("Ali", 100, 0.05)
    s.add_interest()
    print(s.describe())              # Savings - Ali: 105.0

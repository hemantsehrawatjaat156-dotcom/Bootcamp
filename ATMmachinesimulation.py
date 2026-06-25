class ATM:
    def __init__(self, pin, balance, owner):
        self.__pin = pin
        self.__balance = balance
        self._owner = owner
        self.__authenticated = False

    def authenticate(self, pin):
        if pin == self.__pin:
            self.__authenticated = True
            print("Login successful")
        else:
            print("Wrong PIN")

    def balance(self):
        return self.__balance

    def withdraw(self, amt):
        if not self.__authenticated:
            print("Please login first")
            return
        if amt > 20000:
            print("Limit is 20000")
            return
        if amt > self.__balance:
            print("Low balance")
            return
        self.__balance -= amt
        print("Withdrawn:", amt)

    def deposit(self, amt):
        if not self.__authenticated:
            print("Please login first")
            return
        self.__balance += amt
        print("Deposited:", amt)

    def mini_statement(self):
        if not self.__authenticated:
            print("Please login first")
            return
        print("Owner:", self._owner)
        print("Balance:", self.__balance)

atm = ATM(1234, 50000, "John Doe")
atm.authenticate(1234)
atm.deposit(5000)
atm.withdraw(10000)
atm.mini_statement()
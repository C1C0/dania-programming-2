class BankAccount:
    def __init__(self, name, balance = 0) -> None:
        self.__set_details(name, balance)

    def __set_details(self, name:str, balance:float = 0) -> None:
        self.__name = name
        self.__balance = balance

    def display(self) -> None:
        print(f"---\nName: {self.__name}\nBalance: {self.__balance}\n---")

    def withdraw(self, amount: float) -> None:
        self.__balance -= amount

    def deposit(self, amount: float) -> None:
        self.__balance += amount
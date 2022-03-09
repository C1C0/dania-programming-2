import factories as fa

from BankAccount import BankAccount
from Book import Book

if __name__ == '__main__':
    acc1 = BankAccount("Acc1")
    acc2 = BankAccount("Acc2", 1000)
    
    acc1.display()
    acc2.display()
    
    acc1.deposit(111)
    acc1.deposit(111)
    
    acc2.deposit(500)
    
    acc1.withdraw(22)
    acc2.withdraw(1000)
    
    acc1.display()
    acc2.display()
    
    ######
    
    b1 = fa.BookFactory()
    b2 = fa.BookFactory()
    b3 = fa.BookFactory()
    b4 = fa.BookFactory()
    
    b1.display()
    b2.display()
    b3.display()
    b4.display()
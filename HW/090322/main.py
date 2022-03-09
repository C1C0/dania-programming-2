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
    
    books = [b1, b2, b3, b4]
    
    for book in books:
        book.display()
    
    beforeSelling = b1.getCopies()
    
    for i in range(beforeSelling):
        b1.sell()
        
    b1.display()
    b1.sell()
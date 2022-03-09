from BankAccount import BankAccount

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
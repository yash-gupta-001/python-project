class Account:
    bank_name="State Bank of India"
    def __init__(self,account_holder):
        self.account_holder=account_holder
        self.balance=0
    def deposite(self):
        balance=int(input("Enter Your Amount: "))
        self.balance+=balance
        
        print("Your Amount Depositted Successfully")
        print("Your available amount is ",self.balance)
        print("========================")
        return
    
    def withdraw(self):
        balance=int(input("Enter Your Amount: "))
        if balance>self.balance:
            print("Insufficiant Balance")
        else:
            self.balance-=balance
            print("Your Amount Withdraw Successfully")
            print("Your available amount is ",self.balance)
            print("========================")
            return
    
    def show_balance(self):
        print("Your available amount is ",self.balance)
        print("========================")

    @classmethod
    def name(cls):
        print(cls.bank_name)
        print("========================")

    def exit_1(self):
        print("Thanks You")
    
system=Account("Yash")


while True:
    print("========================")
    print("1. Press 1 to Deposite ")
    print("2. Press 2 to Withdraw ")
    print("3. Press 3 to Check Balance  ")
    print("4. Press 4 to Check Bank Name ")
    print("5. Press 5 to Exit ")
    print("========================")

    choice=int(input("Enter Your Choice: "))
    if choice==1:
        system.deposite()
    elif choice==2:
        system.withdraw()
    elif choice==3:
        system.show_balance()
    elif choice==4:
        Account.name()
    
    elif choice==5:
        system.exit_1()
    else:
        print("You Entered Wrong Number")

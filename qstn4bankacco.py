class Account:

    def __init__(self,title=None,balance=0):
         self.title=title
         self.balance=balance
                

class SavingsAccount(Account):

    def __init__(self,title=None,balance=0,interestrate=0):
        super().__init__(title, balance)
        self.interestRate = interestrate
obj1=Account("Ashish",5000)
obj2=SavingsAccount("Ashish",5000,5)
        
    
class CustomerAccount:
  2 
  3         def __init__(self,customer_id:str,customer_name:str,account_balance:int):
  4             self.customer_id=customer_id
  5             self.customer_name=customer_name
  6             self.account_balance=account_balance
  7             self.transaction_log=TransactionLog()
  8 
  9 
 10 
 11         def deposit(self,amount:int):
 12             self.account_balance+=amount
 13             self.transaction_log.log_transaction(f'Transaction deposit with an ammount of {amount} ')
 14 
 15         def withdraw(self,amount:int):
 16             self.account_balance-=amount
 17             self.transaction_log.log_transaction(f'Transaction withdraw with an ammount of {amount} ')
 18 
 19 class TransactionLog:
 20 
 21         def log_transaction(self,transaction_details:str):
 22             self.transaction_details=transaction_details
 23             print(self.transaction_details)
 24 
 25 
 26 customer=CustomerAccount('12345','Adam Smith',200000)
 27 
 28 
 29 customer.deposit(50000)
 30 
 31 print(customer.account_balance)
 32 
 33 
 34 #The issue is that  we can access the class properties directly which can cause logicalerrors
 35 
 36 
 37 
 38 
 39 
 40 
~                                                                                                                                              
~                                

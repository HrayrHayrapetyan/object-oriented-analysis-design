
import time
class TimeZone:
    def __init__(self, offset_minutes, abbreviation):
        self.offset_minutes = offset_minutes
        self.abbreviation = abbreviation

    def __str__(self):
        return (f"{self.abbreviation} (UTC{'+' if self.offset_minutes >= 0 else '-'}{abs(self.offset_minutes) // 60}:"
                f"{abs(self.offset_minutes) % 60:02d})")

    @property
    def offset_minutes(self):
            return self.__offset_minutes

    @offset_minutes.setter
    def offset_minutes(self,value):
            self.__offset_minutes=int(value)

class ConfirmationNumber:
        def __init__(self,transaction_type:str,account_number:str,time_zone:TimeZone,transaction_id:int):
                self.transaction_type=transaction_type
                self.account_number=account_number
                self.time_zone=time_zone
                self.transaction_id=transaction_id

        @property
        def transaction_type(self):
            return self.__transaction_type

        @transaction_type.setter
        def transaction_type(self, value):
            self.__transaction_type = value

        @property
        def account_number(self):
            return self.__account_number

        @account_number.setter
        def account_number(self, value):
            self.__account_number = value

        @property
        def time_zone(self):
            return self.__time_zone

        @time_zone.setter
        def time_zone(self, value):
            self.__time_zone = value

        @property
        def transaction_id(self):
            return self.__transaction_id

        @transaction_id.setter
        def transaction_id(self, value):
            self.__transaction_id = value


class BankAccount:
    transactionid=0
    interest_rate=0.5

    def __init__(self,firstname:str,lastname:str,account_number:str,timezone:TimeZone,balance:float):
            self.account_number=account_number
            self.firstname=firstname
            self.lastname=lastname
            self.timezone=timezone
            self.balance=balance

    def GetFullName(self):
            return self.__firstname + '' + self.__lastname

    @property
    def account_number(self):
            return self.__account_number

    @account_number.setter
    def account_number(self,value):
        self.__account_number=value

    @property
    def firstname(self):
        return self.__firstname

    @firstname.setter
    def firstname(self, value):
        if isinstance(value,str):
                self.__firstname = value

    @property
    def lastname(self):
        return self.__lastname

    @lastname.setter
    def lastname(self, value):
        if isinstance(value, str):
            self.__lastname = value

    @property
    def timezone(self):
        return self.__timezone

    @timezone.setter
    def timezone(self, value):
        if isinstance(value,TimeZone):
                     self.__timezone = value

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, value):
        if isinstance(value,int) and value>0:
            self.__balance = value

    def get_transaction(self,confirm_num:ConfirmationNumber):
            return (f'{confirm_num.transaction_type} - {confirm_num.account_number} - '
                    f'{confirm_num.time_zone} - {confirm_num.transaction_id}')


    def deposit(self,deposit:int):
            if deposit>0:
                    self.__balance+=deposit
            BankAccount.transactionid+=1
            confirm_num=ConfirmationNumber('D',self.account_number,self.timezone,BankAccount.transactionid)
            return self.get_transaction(confirm_num)

    def withdrawal(self,withdrawal):
            if self.__balance>withdrawal:
                    self.__balance-=withdrawal
                    BankAccount.transactionid += 1
                    confirm_num= ConfirmationNumber('W', self.account_number, self.timezone, BankAccount.transactionid)
            else:
                    confirm_num= ConfirmationNumber('X', self.account_number,self.timezone, BankAccount.transactionid)
            return self.get_transaction(confirm_num)



    def pay_interest(self):
            if self.__balance>self.__balance*BankAccount.interest_rate/100:
                self.__balance-=self.__balance*BankAccount.interest_rate/100
                BankAccount.transactionid+=1
            confirm_num= ConfirmationNumber('I', self.account_number, self.timezone, BankAccount.transactionid)
            return self.get_transaction(confirm_num)



account1=BankAccount('Brad','Smith','23123131',TimeZone('-120','PST'),1500)
print(account1.deposit(1000))
print(account1.withdrawal(2000))
print(account1.pay_interest())

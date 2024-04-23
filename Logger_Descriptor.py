import weakref
import re
from datetime import datetime
class NumericRange:
    Min=10
    Max=100
    def __init__(self):
        self.value=weakref.WeakKeyDictionary()

    def __get__(self,instance,owner):
        if instance is None:
            return self
        getattr(self.value,instance)

    def __set__(self,instance,value):
        if value not in range(self.Min,self.Max):
            raise ValueError('Number not in range')
        previous_value=self.value.get(instance,'None')
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.value[instance]=value
        print(f'Logged the number  {value}, previous - {previous_value}, current time - {current_time}')



class StringValue:
    def __init__(self):
        self.value=weakref.WeakKeyDictionary()

    def __get__(self,instance,owner):
        if instance is None:
            return self
        return getattr(self.value,instance)

    def __set__(self,instance,value):
        pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        if not re.match(pattern,value):
            raise ValueError('string is not valid')
        previous_value=self.value.get(instance,'None')
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.value[instance]=value
        print(f'Logged the string  {value}, previous - {previous_value}, current time - {current_time}')

class User:
    logs=[]
    age=NumericRange()
    email=StringValue()

u1=User()
u1.age=99
u1.email='2123@gmail.com'
u1.email='hello@gmail.com'
u2=User()
u2.age=23
u2.age=45
u2.email='123@yahoo.com'
u2.email='wdwdwdwdw@gmail.com'



import weakref
import re

class ValidString:
    def __init__(self):
        self.value=weakref.WeakKeyDictionary()
    def __get__(self,instance,owner):
        if instance is None:
                return self
        return getattr(self.value,instance)

    def __set__(self,instance,value):
        if not isinstance(value,str):
                raise (TypeError('Wrong Type'))
        self.value[instance]=value
class IntegerValue:
    def __init__(self):
        self.value=weakref.WeakKeyDictionary()

    def __get__(self,instance,owner):
        if instance is None:
            return self
        return getattr(self.value,instance)

    def __set__(self,instance,value):
        if not isinstance(value,int):
            raise TypeError('Wrong Type')
        if value<=0:
            raise ValueError('Age cant be a negative number or a zero')
        self.value[instance]=value


class ValidEmail:

    def __init__(self):
        self.value=weakref.WeakKeyDictionary()

    def __get__(self,instance,owner):
        if instance is None:
            return self
        return getattr(self.value,instance)

    def __set__(self,instance,value):
        pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        if not re.match(pattern,value):
            raise ValueError('email is not valid')
        self.value[instance]=value

class ValidPass:

    def __init__(self):
        self.value=weakref.WeakKeyDictionary()

    def __get__(self,instance,owner):
        if instance is None:
            return self
        return getattr(self.value,instance,'Non-Value')

    def __set__(self,instance,value):
        SpecialSym = ['$', '@', '#', '%']
        if not isinstance(value,str):
            raise TypeError('Wrong Type')
        if len(value)<8:
            raise ValueError('Pass should be more then 8 characters')
        if len(value)>20:
            raise ValueError('Pass should be less then 20 characters ')
        if not any(char.isdigit() for char in value):
            raise ValueError('Pass should have at least one numeral ')
        if not any(char.isupper() for char in value):
            raise ValueError('Pass should have at least one uppercase character')
        if not any(char.islower() for char in value):
            raise ValueError('Pass should have at least one lowercase character')
        if not any(char in SpecialSym for char in value):
            raise ValueError('Pass should have at least one of the special symbols')
        self.value[instance]=value

class User:
        first_name=ValidString()
        last_name=ValidString()
        password=ValidPass()
        email=ValidEmail()
        age=IntegerValue()

u1=User()
u1.first_name='Bob'
u1.last_name='Brown'
u1.email='Hello@gmail.com'
u1.password='Aa@12345678'
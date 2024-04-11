class User:
        def __init__(self,name:str,id:str,age:int):
                    self.name=name
                    self.id=id
                    self.age=age
        @property
        def name(self):
                return self.__name

        @name.setter
        def name(self,name:str):
                if isinstance(name,str):
                        self.__name = name

        @property
        def id(self):
                return self.__id

        @id.setter
        def id(self,id:str):
                if isinstance(id,str):
                        self.__id=id

        @property
        def age(self):
                return self.__age

        @age.setter
        def age(self,age:int):
                if isinstance(age,int):
                        self.__age=age

class Logger:
        def Log_in(self,user:User):
                    print(f'Logged in User {user.name}, age - {user.age}, id - {user.id}')

class EmailNotifier:
        def send_email(self,user:User):
                print(f'Email Notification Sent To The User {user.name}')


class InAppNotifier:
        def send_InApp(self,user:User):
                print(f'InApp Notification Sent To The User {user.name}')

class PushNotifier:

        def send_Push(self,user:User):
                print(f'Push Sent To The User {user.name}')

class ProjectManager(Logger,EmailNotifier,InAppNotifier,PushNotifier):









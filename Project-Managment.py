class User:
    def __init__(self, name: str, id: str, age: int):
        self.name = name
        self.id = id
        self.age = age

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        if isinstance(name, str):
            self.__name = name

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id: str):
        if isinstance(id, str):
            self.__id = id

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age: int):
        if isinstance(age, int):
            self.__age = age


class Logger:
    def Log(self, message):
        print(f'Logged the message {message}')


class EmailNotifier:
    def send_email(self, user: User):
        print(f'Email Notification Sent To The User {user.name} ')


class InAppNotifier:
    def send_InApp(self, user: User):
        print(f'InApp Notification Sent To The User {user.name} ')


class PushNotifier:

    def send_Push(self, user: User):
        print(f'Push Notification Sent To The User {user.name} ')


class TeamMember(Logger,InAppNotifier,PushNotifier):
        def assign_project(self,user:User,project:str):
                self.Log(f'TeamMember delivered the project {project} to the user {user}')
                self.send_Push(user)
                self.send_InApp(user)

class ProjectManager(Logger, EmailNotifier, InAppNotifier, PushNotifier):

        def assign_project(self,user:User,project:str,team_member:TeamMember):
            self.Log(f'pm assigned a project "{project}" to the user {user}')
            self.send_email(user)
            team_member.assign_project(user,project)



class ExternalContractor(TeamMember,ProjectManager):
        pass





#1- Abstract class va methoddan foydalanilgan yuli
from abc import ABC, abstractmethod

class Person(ABC):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @abstractmethod
    def display_info(self):
        pass

class User(Person):
    def display_info(self):
        print(f"User: {self.name}, Age: {self.age}")

class Admin(Person):
    def display_info(self):
        print(f"Admin: {self.name}, Age: {self.age}")\


user = User("John Doe", 25)
admin = Admin("Admin Name", 30)

user.display_info()
admin.display_info()




#2- Abstract class va methoddan foydalanilmagan yuli

class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        pass

class User(Person):
    def display_info(self):
        print(f"User: {self.name}, Age: {self.age}")

class Admin(Person):
    def display_info(self):
        print(f"Admin: {self.name}, Age: {self.age}")\


user = User("John Doe", 25)
admin = Admin("Admin Name", 30)

user.display_info()
admin.display_info()

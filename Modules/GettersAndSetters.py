

# Add a variable age and create a getter and setter
class Person:

    def __init__(self,age,gender,name):
        self.age = age
        self.gender = gender
        self.name = name

    def set_age(self,age):
        self.age = age
        print(self.age)
        return self.age

    def get_age(self):
        print(self.age)
        return  self.age


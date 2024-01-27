class Person:

    def __init__(self, name, age, gender):
        self.__name = name
        self.__age = age
        self.__gender = gender

    @property
    def Name(self):
        return self.__name
    #no method overloading in python
    @Name.setter
    def Name(self, value):
        self.__name = value
    @property
    def Age(self):
        return self.__age
    @Age.setter
    def Age(self, value):
        #cannot age backwards
        if self.__age < value:
            self.__age = value
    @staticmethod

#dont have to initialize an object
Person.mymethod()
        
p1 = Person("Mike",20,'m')
print(p1.Name)
p1.Age = 21
print(p1.Age)
#produces error, no attribute
print(p1.__age)
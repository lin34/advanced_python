#promotes separation of concerns
#The definition of an abstract class is that we cannot make instances of it

from abc import ABCMeta, abstractstaticmethod

class IPerson(metaclass=ABCMeta):

    @abstractstaticmethod
    def person_method():
        '''interface method'''

class Student(IPerson):

    def __init__(self):
        self.name = "Basic student name"

    def person_method(self):
        print("I am a student")
    
class Teacher(IPerson):
    def __init__(self):
        self.name = "Basic Teacher Name"

    def person_method(self):
        print("I am a teacher")

class PersonFactory:

    @staticmethod
    def build_person(person_type):
        if person_type == "Student":
            return Student()
        if person_type() == "Teacher":
            return Teacher()
        print("Invalid Type")
        return -1

#dynamically build a teacher or student at run time
if __name__ == "__main__":
    choice = input("What type of person do you want to create?\n")
    person = PersonFactory.build_person(choice)
    person.person_method()



#cannot do this
p1 = IPerson()
p1.person_method()

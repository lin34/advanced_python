#Magic Methods & Dunder
class Person:

    def __init__(self,name, age):
        self.name = name
        self.age = age
    def __del__(self):
        print("Object is being deconstructed")
p = Person("Mike", 25)

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __repr__(self):
        return f"X: {self.x}, Y: {self.y}"

    def to_string(self):
        return

    def __len__(self):
        return 10
    
    def __call__(self):
        print("Hello, I was called!")
v1 = Vector(10,30)
v2 = Vector(50, 60)
v3 = v1 + v2
v3()#call the object
print(v3)
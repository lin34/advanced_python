class Parent:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Hello, my name is {self.name}")

class Child(Parent):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age
    def greeting(self):
        super().greet()
        print(f"I am {self.age} years old")

# Example usage
child = Child("Alice", 5)
child.greet()
def mydecorator(function):
    def wrapper(*args, **kwargs):
        return_value = function(*args, **kwargs)
        print("I am decorating your function")
        return return_value
    return wrapper

@mydecorator
def hello(person):
    return f"Hello {person}"

print(hello("Mike"))

def example_function(*args, **kwargs):
    for arg in args:
        print(arg)
    for key, value in kwargs.items():
        print(key, ":", value)

example_function(1, 2, 3, name="John", age=25)

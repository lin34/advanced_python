#mypy checks for consistency of type hinting
#type errors are not checked in python.
#can use type hinting

def myfunction(myparameter: int) -> int:
    return myparameter + 10

def otherfunction(otherparameter: str):
    print(otherparameter)

otherfunction(myfunction(20))

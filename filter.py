#filter(function, iterable)

#define a function to check if even

def is_even(num):
    return num % 2 == 0

numbers = [1,2,3,4,5,6,7,8,9]

#use a filter to get a list of numbers
even_numbers = list(filter(is_even, numbers))
even_numbers2 = list(filter(lambda x:x % 2 == 0, numbers))
print(even_numbers)


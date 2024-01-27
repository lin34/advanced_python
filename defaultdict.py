from collections import defaultdict

tuple_list = [("A", 10), ("B", 4), ("A", 5), ("C", 7), ("B", 1)]

grouped_data = defaultdict(list)

for key, value in tuple_list:
    grouped_data[key].append(value)

print(grouped_data)
 
class MyDefaultDict(defaultdict):

    def __missing__(self, key):
        self[key] = value = len(key)
        return value

test = MyDefaultDict()

print(test["hello"])
print(test["hi"])
print(test)
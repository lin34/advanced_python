#lambda arguments: expression

#Regular function
def add(x, y):
    return x + y

#equivalent lambda function
add_lambda = lambda x, y: x + y

# Using the lambda function
result = add_lambda(2,3)
print(result)

#using a sort function
points = [(1,2), (0,3), (4,1), (3,0)]

# Sort based on the sum of x and y coordinates
sorted_points = sorted(points, key = lambda point: point[0] + point[1])

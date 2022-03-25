"""
1Write a map function that adds plus 5 to each item in the list.
2Write a map function that returns the squares of the items in the list.
3Using the filter() function filter the list so that only negative numbers are left.
4Using the filter function, filter the even numbers so that only odd numbers are passed to the new list.
5Create a lambda function that takes one parameter (a) and returns it.
6Write a Python program to create a lambda function that adds 15 to a given number passed in as an argument. Print the result.
7Create a lambda function that multiplies argument x with argument y and prints the result.
8Write a Python program to filter (even and odd) a list of integers [1,2,3,4,5,6,7,8,9,10] using Lambda
9Write a Python program to square and cube every number in the list of integers [1,2,3,4,5,6,7,8,9,10] using Lambda.
10Write a Python program that multiplies each number of the list [2, 4, 6, 9, 11] with 2 using the lambda function. Print the result
"""

hwList = [-1, -2, -3, -4, -5, -6, -7, -8, -9, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# 1
newList = list(map(lambda x: x + 5, hwList))

# 2
newList = list(map(lambda x: x * x, hwList))

# 3
newList = list(filter(lambda x: x < 0, hwList))

# 4
newList = list(filter(lambda x: x % 2 != 0, hwList))

# 5
lambdaTest = lambda x: x

# 6
print((lambda x: x + 15)(20))

# 7
print((lambda x, y: x * y)(10, 20))

# 8
hwList2 = [1,2,3,4,5,6,7,8,9,10]
newListEven = list(filter(lambda x: x % 2 == 0, hwList))
newListOdd = list(filter(lambda x: x % 2 != 0, hwList))

# 9
newList = list(map(lambda x: x * x, hwList2))

# 10
hwList3 = [2, 4, 6, 9, 11] 
newList = print(list(map(lambda x: x * 2, hwList3)))
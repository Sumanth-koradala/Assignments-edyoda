# 1. Write a Python program to create a lambda function that adds 25 to a given number passed in as an argument.


x = lambda x : x+ 25

print("Number after adding 25:", x(10))







# 2. Write a Python program to triple all numbers of a given list of integers. Use Python map.


num = 1,2,3,4,5,6

s = map(lambda x : x + x + x, num)

print("Numbers after triple:", list(s)) 





# 3. Write a Python program to square the elements of a list using map() function.


numbers = [2,4,6,8]

def square(num):
	return num ** 2

sq_num = list(map(square, numbers))


print("Elements after square:",sq_num) 
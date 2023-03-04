# 1. lets play with fibanacci
 
num1 = 0
num2 = 1
for i in range(10):
    print(num1)
    next_num = num2 + num1
    num1 = num2
    num2 = next_num  



#for space in output
print("    ")


# 2. Send the words to mirror dimension

s = "python sample string"

print("mirror dimension word :" ,s[::-1])  



#for space in output
print("      ")


# 3. Dont go outside in odd day

l = [1,25,76,98,99,990,745,12,3]

even_num = 0
odd_num = 0

for value in l:
    if(value % 2 == 0):
       even_num = even_num + 1
    else:
        odd_num = odd_num + 1

print("number of even numbers :", even_num)
print("number of odd_num :", odd_num)   
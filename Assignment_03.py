#1. Write a Python function to sum all the numbers in a list.

def sum(l):

  total = 0
  for items in l:
    total = total + items
  
  return total

list = [11,22,33,44,55]

print("Sum of all numbers in the list:", sum(list))



print("     ") #for space in output



#2. Write a Python program to reverse a string.


def reverse_val(value):
    reverse = value[::-1]
    return reverse

s = "1234AbCd"

result = reverse_val(s)
print(("Reverse output of a string:") , result)  



print("    ")  #for space in output


#3. Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters.



def char(string):
  uppers = 0
  lowers = 0
  for i in string:
    if i.isupper():
      uppers += 1
    elif i.islower():
      lowers +=1
    else:
      pass
  return("Number of upper char:",uppers),("Number of lower char:" ,lowers)

print(char("Hello Team EdYoda"))  
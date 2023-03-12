# 1. Write a Python program to get a list, sorted in increasing order by the last element in each tuple from a given list of non-empty tuples


s = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1),(9,0)]


def value(items):
    return items[-1]

sorted_value = sorted(s, key = value)

print(sorted_value)



print('       ')  # for space in output




#2. Write a Python program to print a dictionary whose keys should be the alphabet from a-z and the value should be corresponding ASCII values


alphabets = "abcdefghijklmnopqrstuvwxyz"

for values in alphabets:
    ascii_val = {values: ord(values)}
    print(ascii_val, end = ' ') 

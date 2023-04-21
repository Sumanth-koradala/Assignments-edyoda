
#Q1. Write a program to find all pairs of an integer array whose sum is equal to a given number?

num = [1,3,4,7,2,8]

sum = 6
b = len(num)


def t_sum(num):
 


    for i in range(0, b):
        for j in range(i+1, b):
            if (num[i] + num[j] == sum):
                return (num[i], num[j])

            
    return -1

print(t_sum(num))  
            

#Q2. Write a program to reverse an array in place? In place means you cannot create a new array. You have to update the original array.

a = [1,2,3,4,5]


def rev_arr(a):
    print(a[::-1])


rev_arr(a)    

    




#Q3. Write a program to check if two strings are a rotation of each other?

a = input("enter string one: ")
b = input("enter rotation string: ")


if a == b[::-1]:
    print("rotated string")

else:
    print("not a rotation")





#Q4. Write a program to print the first non-repeated character from a string?

def nonrepeat(string):

    freq = {}

    for x in string:
        freq[x] = freq.get(x,0) + 1

    for i in string:
        if freq[i] == 1:
            return i
        
    return -1

print("first non-repeated character is: ", (nonrepeat("abcabcabcde")))



#Q5. Read about the Tower of Hanoi algorithm. Write a program to implement it.


def hanoi_tow(a, from_rod, to_rod, aux_rod):
    if a == 0:
        return
    hanoi_tow(a-1, from_rod, aux_rod, to_rod)
    print("Move disk", a, "from rod", from_rod, "to rod", to_rod)
    hanoi_tow(a-1, aux_rod, to_rod, from_rod)
  
  
b = 3
hanoi_tow(b, 'A', 'C', 'B')








#Q6. Read about infix, prefix, and postfix expressions. Write a program to convert postfix to prefix expression.














#Q7. Write a program to convert prefix expression to infix expression.















#Q8. Write a program to check if all the brackets are closed in a given code snippet.

def par_check(x):
    st = []

    for char in x:
        if char in "({[":
            st.append(char)

        elif char == ")":
            if(not st or st[-1] != "("):
                return False
            st.pop()

        elif char == "]":
            if (not st or st[-1] != "["):
                return False
            st.pop()

        elif char == "}":
            if(not st or st[-1] != "{"):
                return False
            st.pop()


    if (not st):
        return True
        
    else:
        return False
        
x = "({[]})"
print(par_check(x))







#Q9. Write a program to reverse a stack.

class stack: 
        def __init__(self):
            self.data = []

        def push(self, elements):
            self.data.append(elements)

        def display(self):
            print(self.data)
        
        def reverse(self):
             rev = self.data[::-1]
             print(rev)





st = stack()
st.push(-2)
st.push(2)
st.push(3)
st.push(4)
print("original stack is: ")
st.display()
print("reversed stack is ")
st.reverse()




#Q10. Write a program to find the smallest number using a stack.

class stack: 
        def __init__(self):
            self.data = []

        def push(self, elements):
            self.data.append(elements)

        def display(self):
            print(self.data)
        
        def small_no(self):
            min = self.data[0]
            for i in range(0, len(self.data)):
                if self.data[i] < min:
                    min = self.data[i]

            print(str(min))


st = stack()
st.push(-2)
st.push(2)
st.push(3)
st.push(4)
print("finding smallest number in this list")
st.display()
print("smallest character in the stack is")
st.small_no()   
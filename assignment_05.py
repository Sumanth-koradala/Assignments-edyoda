#Challenge 1: Square Numbers and Return Their Sum

class point:
	def __init__ (self,x,y,z):
		self.x = x
		self.y = y 
		self.z = z

	def sqno(self,x,y,z):
		y= ((x**2),(y**2),(z**2))
		print("sum of squared numbers:",sum(y))


obj = point(1,2,3)
obj.sqno(2,3,4)
	

print("   ")    # for space in output



#Challenge 2. Implementing a calculator class


class calculator:
	def __init__(self,num1, num2):
		self.num1 = num1
		self.num2 = num2

	def addition(self, num1,num2):
		print ("Addition:" ,num1 + num2)

	def subtraction(self, num1 , num2):
		print("Subtraction:",num2 - num1)

	def multiplication(self, num1 ,num2):
		print("Multiplication:", num1*num2)

	def division(self, num1, num2):
		print("Division:",num2 / num1)

a = int(input("enter num1:"))
b = int(input("enter num2:"))

obj = calculator(a,b)

obj.addition(a,b)
obj.subtraction(a,b)
obj.multiplication(a,b)
obj.division(a,b)   



print("   ")    # for space in output



#Challenge 3: Implement the Complete Student Class

class student:
	def __init__(self):
		self.__name = "raju"
		self.__rollno = 1001

	def name(self):
		print("name of student: {}".format(self.__name))

	def namegetter(self,new_name):
		self.__name = new_name


	def rollno(self):
		print("roll numbe of the student: {}".format(self.__rollno))
    

	def rollnogetter(self,new_rollno):
		self.__rollno = new_rollno


obj = student()


obj.name()

str(obj.namegetter("ram"))
obj.name()


obj.rollno()

obj.rollnogetter(1002)
obj.rollno()   




print("   ")    # for space in output





#Challenge 4: Implement a Banking Account

class account:
	def __init__(self,title,balance):
		self.title = 0
		self.balance = 0


class savingsaccount(account):
	def __init__(self, title, balance, interestrate):
		super().__init__(title, balance)
		interestrate = 5

	def savings(self,title,balance, interestrate):
		print(title, balance, interestrate)

obj = savingsaccount("ashish", 5000, 5)


obj.savings("ashish", 5000, 5) 



print("   ")    # for space in output



#Challenge 5: Handling a Bank Account


class get_balance:
	def __init__(self,balance):
		self.balance = balance 
		return balance 

	def deposit(self,balance,deposit):
		amount = balance + deposit
		

	def withdrawl(self,balance,amount):
		wtdrl = balance - amount
		return wtdrl 


class savings_ac(get_balance):
	def __init__(self,balance, interest_rate):
		super().__init__(balance)
		self.interest_rate = interest_rate

	def interest_amount(self,interest_rate,balance):
		int_amt = interest_rate * balance /100
		print("innterest amount of the balance is:", int_amt)

obj = savings_ac(2000,5)
obj.interest_amount(2000, 5)




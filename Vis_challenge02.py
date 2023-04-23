    
import datetime


print("        Welcome to JOBme.com        \n")

print("Lets start finding your dream job\n")


print("Please enter your details below") 

a = input("Enter your first name: ")
b = input("Enter your second name: ")
x = print("WELCOME", a, b)

c = input("Enter your professional email address: ")
d = int(input("Please your contact details: "))
e = input("Please enter your martial status: ")



print("Please select your Education Qualification:")
ed_det= ["00. Intermediate", "01. Graduation", "02. Post Graduation"]

for i in ed_det:
    print(i)

sel = int(input("please enter the index number to select your education qualification: "))
f = print(ed_det[sel])  

print("Please select your Gender: ")
gen_det = ["00. Male", "01. Female", "02. Other"]

for i in gen_det:
    print(i)

select = int(input("please enter the index number to select your gender: "))
g = print(gen_det[select])  


now = datetime.datetime.now()
print(now)

h = int(input("Please enter your age as of above date: "))

if h <= 17:
    print("********Sorry you are not eligible for any jobs********\nYou have to be above 18")
    
else:
    pass


i = input("PLease enter your Date of Birth(dd-mm-yy): ")  


j = input("Please enter your current address: ")
k = input("Please enter your permanent address,(enter SAME if same as current address): ")

if k == "same":
    print(j) 
else:
    print(j,"\n", k)     



dec = input("DECLARATION:\nI declare that all the facts given above are genuine to the best of my knowledge and belief. \nPlease type yes: ")

if dec == "yes":
    print("Application submitted successfully")
else:
    print("Please give correct details and enter YES")
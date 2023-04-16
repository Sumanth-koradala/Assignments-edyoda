
print("-----WELCOME TO LA PARADISE RESTAURANT-----")

print("please enter the following details to login : ")


f_name = input("Please enter your FULL NAME: ")
print("WELCOME" , f_name)
a = ((input("Enter your PHONE NUMBER: ")))
b = (input("Enter your Email Address: "))
c = (input("Enter DELIVERY ADRESS: "))
d = (input("Enter your password: "))        
 





welcome = ["00. place new order", "01. Show order history", "2. update profile"]

for i in welcome:
    print(i)



x = int(input("Enter the index number to select an option: "))




if x == 0:
    food_items = ["0.TANDOORI CHICKEN", "1.VEGAN BURGER   ", "2.TRUFFLE CAKE   "]

    price_food_items = [240,320,900]

    details_of_food = ["4 pieces", "1 piece", "900 grams"]

    for i in food_items:
        print(i)

    end = " "

    booking = int(input("Please enter the index number of item to book your order: "))

    print("item","      ", "      price"," ", "quantity")

    print(food_items[booking][2::],":", price_food_items[booking], ":", details_of_food[booking])


    print("Please comfirm your order: ",food_items[booking][2::])

    print("---Hurrah you have availed the discount of 50 rupees on your order ---")





    if booking == 0:
        print("order of", food_items[booking][2::],"of price", price_food_items[booking] -50 , "confirmed")
        
            

    if booking == 1:
         print("order of", food_items[booking][2::],"of price", price_food_items[booking]- 50, "confirmed")
        

    if booking == 2:
         print("order of", food_items[booking][2::],"of price", price_food_items[booking]- 50, "confirmed")

    print("ENJOY YOUR MEAL :)")

elif x == 1:
    print("No orders yet")

elif x == 2:
    s = f_name.replace(f_name, input("Enter your new Name: " ))
    print(s)
    s1= a.replace(a,(input("Enter your PHONE NUMBER: ")))
    print(s1)
    s2 = b.replace(b, input("Enter your Email Address: "))
    print(s2)
    s3 = c.replace(c, input("Enter DELIVERY ADRESS: "))
    print(s3)
    s4 = d.replace(d, input("Enter your password: "))
    print(s4)

    print("------DETAILS UPDATED SUCCESSFULLY------")




    



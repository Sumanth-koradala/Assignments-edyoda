import datetime 



print("------- WELCOME TO THE CHICKEN COMPANY -------")
print("What's on your mind today")

food_items = ["0.Beverages", "1.Pizzas   ", "2.Burgers   ", "3.Biryanis  ", "4.Sandwiches "]

price_food_items = [50,300,280,400,280]

details_of_food = ["1 litre", "12 inches", "Medium Sized", "Good To Go For Two", "4 Slices"]

for i in food_items:
    print(i)

end = " "

x = int(input("Please enter the s.no of food_item for AVERAGE price and details: "))

print("item","      ", "price"," ", "quantity")

print(food_items[x][2::],":", price_food_items[x], ":", details_of_food[x])


print("For Items Of " , food_items[x][2::], "Check Below ")













if x == 0:
    a = int(input("Enter 1 For CHILLED WATER BOTTLE" " And" " " "2 for THUMSUP: "))
    if a == 1:
        print("Chilled Water Bottle Coming Right Up.....")
    elif a == 2:
        print("Thumsup Coming Right Up.....")
    else:
        print("please enter number 1 or 2")
    
    

if x == 1:
    b = int(input("Enter 1 for PANEER DELIGHT PIZZA - 300/- , 2 for GOLDEN CORN PIZZA - 320/-: "))
    if b == 1:
        print("PANEER DELIGHT PIZZA Coming Right Up.....")
    elif b == 2:
        print("GOLDEN CORN PIZZA Coming Right Up.....")
    else:
        print("please enter number 1, 2 0r 3")



if x == 2:
    c = int(input("Enter 1 for POTATO BURGER - 180/-, 2 for CORN CAPSICUM CHEESE BURGER - 220/-: "))
    if c == 1:
        print("POTATO BURGER coming right up.....")
    elif c == 2:
        print("CORN CAPSICUM CHEESE BURGER coming right up.....")
    else:
        print("please enter number 1 or 2")



if x == 3:
    d = int(input("Enter 1 for SPICY HYDERABADI CHICKEN BIRYANI - 400/-, 2 for VEG BIRYANI- 250/-: "))
    if d == 1:
        print("SPICY HYDERABADI CHICKEN BIRYANI coming right up.....") 
    elif d == 2:
        print("VEG BIRYANI coming right up......")
    else:
        print("please enter number 1 or 2")


if x == 4:
    e = int(input("Enter 1 for veg grilled sandwich - 150\- : "))
    if e == 1:
        print("VEG GRILLED SANDWICH coming right up......")
    else:
        print("please enter number 1 for veg grilled sandwich")


if x == 5:
    print("SHAWARMA coming right up.....")


print("Amount including taxes: " , price_food_items[x])

print("Total Amont After Discount: ", price_food_items[x] - 70)

now = datetime.datetime.now()
print(now)

print("------THANKYOU VISIT AGAIN------")


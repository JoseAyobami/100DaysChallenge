#  Control Flow with if/else and conditional operators

# Synthax for writing if/else
condition = 0
if condition:
    print()
else: 
    print()    


# Example 
# print("Welcome to the rollercoaster!") 
# height = int(input("What is your height in cm? "))

# if height >= 120:
#     print("You can ride the rollercoaster")
#     age = int(input("What is your age? "))
#     if age <= 12:
#         print("")
#     if age <= 18:
#         print("Please pay $7.")
#     else:
#         print("Please pay $12.")    
# else:
#     print("Sorry you have to grow taller before you can ride.") 


# number_to_check = int(input("Enter a number: "))

# if number_to_check % 2 == 0:
#     print("Number entered is even ")
# else:
#     print("Number entered is odd")    


#  Nested if statements and elif statements
# Example 
# print("Welcome to the rollercoaster!") 
# height = int(input("What is your height in cm? "))

# if height >= 120:
#     print("You can ride the rollercoaster")
#     age = int(input("What is your age? "))
#     if age <= 12:
#         print("Please pay $5.")
#     elif age <= 18:
#         print("Please pay $7.")
#     elif age <=22:
#         print("Please pay $10")    
#     else:
#         print("Please pay $12.")    
# else:
#     print("Sorry you have to grow taller before you can ride.") 

# Coding Challenge
print("Welcome to the rollercoaster!") 
height = int(input("What is your height in cm? "))
bill = 0
if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))

    if age <= 12:
        bill = 5
        print("Child tickets are $5.")
    elif age <= 18:
        bill = 7
        print("Youth tickets are $7.") 
    elif age >= 45 and age <= 55:
        print("Have a free ride with us!")    
    else:
        bill = 12
        print("Adults tickets are $12.") 

    wants_photo = input("Do you want to have a photo take? Type y for Yes and n for No.") 
    if wants_photo == "y":
        # Add $3 to their bill
        bill += 3
    print(f"Your final bill is ${bill}")    
else:
    print("Sorry you have to grow taller before you can ride.") 
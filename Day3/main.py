# Coding Challenge
# Pizza Order Practice

# print("Welcome to Python Pizza Deliveries!")
# size = input("What size do you want? S, M or L: ")
# pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
# extra_cheese = input("Do you want extra cheese? Y or N: ")

# todo: work out how much need to pay based on their size choice
# bill =  0
# if size == "S":
#     bill += 15
# elif size == "M":
#     bill += 20
# elif size == "L":
#     bill += 25
# else:
#     print("You typed the wrong amount")


# todo: work out how much to add to their bill based on their pepperoni choice.
# if pepperoni == "Y":
#     if size == "S":
#         bill += 2
#     else:
#         bill += 3


# todo: work out their final amount based on whether if they want extra cheese
# if extra_cheese == "Y":
#     bill += 1


# print(f"Your final bill is {bill}")    

# Coding challenge 2
print("Welcome to Treasure island.")
print("Your mission is to find the treasure.")
side_check = input("Choose from left or right? L or R ")


if side_check == "L":
    next_phase1 = input("You move to the stage 1."
    "Choose between swim or wait? S or W ")    
    if next_phase1 == "W":
        print("Thank for waiting!")
        next_phase2 = input("Choose which door, (Red or Blue or Yellow)? ").lower()
        if next_phase2 == "red":
            print("You enter into lake of red fire. Game over")
        elif next_phase2 == "yellow":
            print("You found the treasure. You win!")

        elif next_phase2 == "blue":
            print("You enter into lake of blue fire. Game over")        
        else:
            print("Game Over") 
    else:
        print("You choose a door that does not exist. Game over")    
                         
else:
    print("Game over")    


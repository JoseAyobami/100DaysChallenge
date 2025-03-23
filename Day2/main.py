# Day 2 Project

print("Welcome to the tip calculator!")
bill = float(input("What is the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 20 0r 15? "))
people = int(input("How many people split the bill? "))
bill_with_tip = (bill / people) * 1.12
print(f"Each person should pay: {bill_with_tip}") 





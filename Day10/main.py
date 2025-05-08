# def is_leap_year(year):
#     """check if a year is a leap year"""
#     if year % 4 == 0:
#         if year % 100 == 0:
#             if year % 400 == 0:
#                 return True
#             else:
#                 return False
#         else:
#             return True
#     else:
#         return False

# years = is_leap_year(year = int(input("Enter a year: ")))
# print(years)

# def is_leap_year(year):
#     # Write your code here. 
#     # Don't change the function name.
#     # check if a year is a leap year
#     if year % 4 == 0:
#         if year % 100 == 0:
#             if year % 400 == 0:
#                 return True
#             else:
#                 return False
#         else:
#             return True
#     else:
#         return False

# all_year = int(input("Enter any year: (example 2000, 1998)"))
# years = is_leap_year(all_year)
# print(years)

def is_leap_year(year):
    # check if a year is a leap year
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
years = [1996, 2000, 1900, 2021]
for year in years:
    if is_leap_year(year):
        print(f"{year} is a leap year.")
    else:
        print(f"{year} is not a leap year.")













# def asking_mamaso(mamaso):
#     """check if i am in love with mamaso"""
#     mamaso = input("Will you be my girlfriend? (yes, no, maybe, i don't know): ").lower()
#     if mamaso == "yes":
#         print("I won big time.. Gonna like her more and more")
#     elif mamaso == "maybe":
#         print("Gonna try more and more")    
#     else:
#         print("I lost big time")


# mamaso_replies = asking_mamaso(["yes", "no", "maybe", "i don't know"])


def add(n1, n2):
    return n1 + n2

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

all_operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

def calculator():
    should_continue = True
    print("Welcome to the calulator")
    user_first_number = float(input("Enter the first number: ")) 

    while should_continue:
        try:
            for symbols in all_operations:
                print(symbols)
            user_operator = input("Select any operator: ")
            user_second_number = float(input("Enter the second number: "))
        except ValueError:
            print("Invalid input. Please enter a number.")

        except ZeroDivisionError:
            print("Cannot divide by zero.")
    
        answer = all_operations[user_operator](user_first_number, user_second_number)
        print(f"{user_first_number} {user_operator} {user_second_number} = {answer}") 

        ask_user = input(f"Do you want to continue? Type y to continue calculating with {answer} or n for 'No': ").lower()
        if ask_user == "y":
            user_first_number = answer
        else:
            should_continue = False
            print("\n" * 20)
            print("Thank you for using the calculator.")
            print("Goodbye")
            calculator()
        
          
calculator()
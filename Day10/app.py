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
    print("Welcome to Stark's Calculator!")
    first_num = float(input("Enter the first number: "))

    while should_continue:
        for symbols in all_operations:
            print(symbols)
        choose_operator = input("Choose an operator: ")
        second_num = float(input("Enter the second num: "))

        answer = all_operations[choose_operator](first_num, second_num)
        print(f"{first_num} {choose_operator} {second_num} = {answer}")

        ask_user = input(f"Do you want to continue? Type y to continue calculating with {answer} or n for 'No': ").lower()
        if ask_user == "y":
            first_num = answer
        else:
            should_continue = False
            print("\n" * 20)    
            calculator()
        

calculator()   











# print(all_operations["*"](3, 4))

# if user_operator in all_operations:


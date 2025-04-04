import random

letters = ["A", "B", "C", "D","E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
symbols = ["@", "#", "$", "%", "^", "&", "*", "."]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

print("Welcome to the PyPassword Generator!")
letters_generate = int(input("How many letters would you like in you password?\n"))
symbols_generate = int(input("How many symbols would you like\n"))
numbers_generate = int(input("How many numbers would you like\n"))


password_list = []
for char in range(0, letters_generate):
    
    # 1 - 4
    password_list.append(random.choice(letters))

for char in range(0, numbers_generate):
    password_list.append(random.choice(numbers))

for char in range(0, symbols_generate):
    password_list.append(random.choice(symbols))


print(password_list)
random.shuffle(password_list)
print(password_list)


password = ""
for char in password_list:
    password += char

print(password)    

# while True:
#     pass



# password = ""

# for char in range(0, letters_generate):
    
#     # 1 - 4
#     password += random.choice(letters)

# for char in range(0, numbers_generate):
#     password += random.choice(numbers)

# for char in range(0, symbols_generate):
#     password += random.choice(symbols)

# print(password)



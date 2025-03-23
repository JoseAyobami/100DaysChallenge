import random


rock = ''' 
_______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)

'''


paper = '''   
     _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)


'''



scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)

'''

game_image = [rock, paper, scissors]


player_choice = int(input("What do you choose? Pick 0 for rock, 1 for paper or 2 for scissors.\n"))
if player_choice >= 0 and player_choice <= 2:
    print(game_image[player_choice])

computer_choice = random.randint(0, 2)
print(f"Computer choose {computer_choice} ")
print(game_image[computer_choice])

if player_choice >= 3 or player_choice < 0:
    print("You typed an invalid number. You Lose!")
elif player_choice == 0 and computer_choice == 2:
    print("You Win!")  
elif computer_choice == 0 and player_choice == 2:
    print("You Lose") 
elif computer_choice > player_choice:
    print("You Lose")        
elif player_choice > computer_choice:
    print("You Win!")
elif computer_choice == player_choice :
    print("It is draw!")    








 
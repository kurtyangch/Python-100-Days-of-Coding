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
import random

hands = [rock, paper, scissors]
player = int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors \n"))
computer = random.randint(0, 2)

print(hands[player])
print("Computer chose\n", hands[computer])

if player == computer:
    print("Draw")
elif player - computer == 1 or player - computer == -2:
    print("You win")
else:
    print("You lose")

from art import logo
import random

print(logo)
number = random.randint(1, 100)

print("Welcome to the Number Guessing Game! ")
print("I'm thinking of a number between 1 and 100")
mode = input("Choose a difficulty: Type 'easy' or 'hard': ")


def easy():
	left = 10
	print(f"You have a {left} attempts remaining to guess a number")
	guess = int(input("Make a guess: "))
	while left!=0:
		if guess == number:
			print("You guess the right number!!")
			break
		elif guess < number:
			print("Too low.\nGuess again.")
			left -= 1
			print(f"You have  {left} attempts remaining to guess a number")
			if left == 0:
				print("You've run out of guess, you lose.")
				break 

			guess = int(input("Make a guess: "))
		else :
			print("Too hight.\nGuess again")
			left -=1
			print(f"You have  {left} attempts remaining to guess a number")
			if left == 0:
				print("You've run out of guess, you lose.")
				break 

			guess = int(input("Make a guess: "))


def hard():
	left = 5
	print(f"You have a {left} attempts remaining to guess a number")
	guess = int(input("Make a guess: "))
	while left != 0:
		if guess == number:
			print("You guess the right number!!")
			break
		elif guess < number:
			print("Too low.\nGuess again.")
			left -= 1
			print(f"You have  {left} attempts remaining to guess a number")
			if left == 0:
				print("You've run out of guess, you lose.")
				break 

			guess = int(input("Make a guess: "))
		else :
			print("Too high.\nGuess again")
			left -= 1
			print(f"You have  {left} attempts remaining to guess a number")
			if left == 0:
				print("You've run out of guess, you lose.")
				break 

			guess = int(input("Make a guess: "))


# easy mode
if mode == "easy":
	easy()

else:
	hard()

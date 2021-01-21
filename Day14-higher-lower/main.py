from game_data import data
from art import logo, vs
import random
from replit import clear
print(logo)
score = 0
game_continue = True
b = random.choice(data)


# format data
def format_data(a):
	a_name = a["name"]
	a_description = a["description"]
	a_country = a["country"]
	return f" {a_name}, a {a_description}, from {a_country}"


# compare (return True or False)
def compare_account(guess, a_follower_count, b_follower_count):
	if a_follower_count > b_follower_count:
		return guess == "A"
	else:
		return guess == "B"


while game_continue:
	# generate 2 random account
	a = b
	b = random.choice(data)
	# A and B can't be the same , no repeated.
	while a == b:
		b = random.choice(data)

	print(f"Compare A: {format_data(a)}")
	print(vs)
	print(f"Against B: {format_data(b)}")

	guess = input("Who has more followers? Type 'A' or 'B' ").upper()
	a_follower_count = a["follower_count"]
	b_follower_count = b["follower_count"]

	clear()
	print(logo)

	# check if user answers correctly
	is_correct = compare_account(guess, a_follower_count, b_follower_count)
	if is_correct:
		score += 1
		print(f"You are right, current score {score}")
	else:
		game_continue = False
		print(f"Sorry, you are wrong, final score {score}")

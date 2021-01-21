from replit import clear
from art import logo
# HINT: You can call clear() to clear the output in the console.
auction = {}
auction_list = []


def add_participant(name, bid):
	auction["Name"] = name
	auction["Bid"] = bid
	auction_list.append(auction)


print(logo)
print("Welcome to the secret auction program.")

play = True
while play:
	name = input("What's your name?\t")
	bid = int(input("What's your bid? \t$"))

	add_participant(name, bid)
	
	ask = input("Are there any other bidder? Type 'yes' or 'no'").lower()
	
	clear()

	if ask == "no":
		values = 0
		for k in auction_list:
			for i, j in auction.items():
				if i == "Bid":
					if j > values:
						values = j
					highest_name = auction_list[auction_list.index(k)]["Name"]
		print(f"{highest_name} is the winner with bid of ${values}")

		play = False



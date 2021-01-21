from art import logo


def add(n1, n2):
	return n1 + n2


def sub(n1, n2):
	return n1 - n2


def multiply(n1, n2):
	return n1 * n2


def div(n1, n2):
	return n1 / n2


operations = {
	"+":add,
	"-":sub,
	"*":multiply,
	"/":div
}


def cal():
	print(logo)
	num1 = float(input("What's the first number? "))
	for k in operations:
			print(k)

	continue_ask = True
	while continue_ask:
		operation_symbols = input("Pick an operation:  ")
		num2 = float(input("What's the next number? "))
		op = operations[operation_symbols]
		answer = op(num1, num2)
		print(f"{num1} {operation_symbols} {num2} = {answer}")
		con = input(f"Please type 'y' to continue calculating with {answer} or type 'n' to start  a nwe calculation:  ").lower()
		if con =="y":
			num1 = answer
		else:
			continue_ask = False
			cal()


cal()

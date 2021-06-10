## if_elif_else.py
def main():
	num = int(input("Type a number: "))
	if num > 0:
		print("this is a positive number.")
	elif num < 0:
		print("this is a negative number.")
	else:
		print("this is zero.")

main()
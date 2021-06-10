## Condition Q3)
def main():
	num = int(input("Type a number: "))
	if num < 0:
		print("the number is less than 0.")
	elif 0 <= num < 10:
		print("the number is greater than or equal to 0 and less than 10.")
	elif 10 <= num < 20:
		print("the number is greater than or equal to 10 and less than 20.")
	else:
		print("the number is greater than 20.")

main()
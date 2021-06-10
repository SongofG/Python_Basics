## is_phone_num.py
def main():
    pnum = input("Cellphone number: ")
    if pnum.isdigit() and pnum.startswith("010"):
        print("OK")
    else:
	    print("No!")

main()


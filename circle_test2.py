# circle_test2.py
from circle import ar_circle
from circle import ci_circle

def main():
    r = float(input("What is radius: "))
    print("Area:", ar_circle(r))
    print("Circumference:", ci_circle(r))

main()

from circle import ar_circle as ac
from circle import ci_circle as cc

def ar_circle(r):
    print("Area:", ac(r))

def ci_circle(r):
    print("Circumference:", cc(r))

def main():
    r = float(input("What is radius: "))
    ar_circle(r)
    ci_circle(r)
    sum = ac(r) + cc(r)
    print("Sum of Area and Circumference: ", sum)

main()


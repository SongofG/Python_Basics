import circle

def main():
    r = float(input("what is the radius: "))
    ar = circle.ar_circle(r)   # circle.py -> ar_circle()
    print("Area:", ar)
    ci = circle.ci_circle(r)
    print("Circumference: ", ci)

main()

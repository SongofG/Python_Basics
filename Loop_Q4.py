# Q1)
def main():
    lcm = 45
    while True:
        if lcm%6==0 and lcm%45==0:
            break
        lcm += 1
    print(lcm)

main()

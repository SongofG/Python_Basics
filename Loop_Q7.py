## Q2)
def main():
    num = 2
    while num < 100:
        num += 1
        if num % 2 == 0 or num % 3 == 0: continue
        print(num, end=' ')

main()

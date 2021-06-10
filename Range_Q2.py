## Q2)
def main(num):
    tpl = tuple(range(1, num+1))
    tpl = tpl + tuple(range(num-1, 0, -1))
    print(tpl)

main(100)

## Q1)
def to_list(tpl):
    lst = []
    for i in tpl:
        lst.append(i)
    return lst

tpl = (1,2,3)
print(tpl)
tpl = to_list(tpl)
print(tpl)

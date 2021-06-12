## Q1)
dc = {"새우깡": 700, '콘치즈':920, '꼬깔콘': 820}
dc['홈런볼'] = 900
print("Q1\n", dc)

## Q2)
for i in dc:
    dc[i] += 100
print("Q2\n", dc)

## Q3)
del dc['콘치즈']
dc['치즈콘'] = 950
print("Q3\n", dc)


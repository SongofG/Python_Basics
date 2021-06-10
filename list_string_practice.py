>>> str = [1,2,3]
>>> len(str)
3
>>> sr = "HaHaHa~"
>>> len(sr)
7
>>> 
>>> st = [1,2,3]
>>> n = len(st)
>>> n
3
>>> def so_simple2(st):
	print(st)
>>> so_simple2([1,3,5])
[1, 3, 5]
>>> # Q1)	
>>> def sum_all(lst):
	sum = 0
	for i in range(len(lst)):
		sum += lst[i]
	return sum

>>> sum_all([1,2,3,4,5])
15
>>> 
>>> # Q2)
>>> def show_reverse(lst):
	for i in range(len(lst)):
		print(lst[-(1+i)], end=' ')
>>> lst = [1,2,3,4,5]
>>> show_reverse(lst)
5 4 3 2 1 
>>> show_reverse("ABCDEFG")
G F E D C B A 
>>> 
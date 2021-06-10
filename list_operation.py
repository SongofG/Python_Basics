>>> ## LIST OPERATIONS
>>> ## Q1)
>>> st = []
>>> st.append(1)
>>> st.append(2)
>>> st.append(3)
>>> st
[1, 2, 3]
>>> st.remove(1)
>>> st.remove(2)
>>> st.remove(3)
>>> st
[]
>>> 
>>> ## Q2)
>>> st = []
>>> st.append(1)
>>> st.append(2)
>>> st.append(3)
>>> st
[1, 2, 3]
>>> st.pop(2)
3
>>> st.pop(1)
2
>>> st.pop(0)
1
>>> st
[]
>>> 
>>> 
>>> ## Q3)
>>> st = [1,2,3,4]
>>> st.clear()
>>> st
[]
>>> st = [1,2,3,4]
>>> st[:] = []
>>> st
[]
>>> 
>>> ## Q4)
>>> st = []
>>> for i in range(10):
	st.append(i+1)

	
>>> st
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> for i in range(10):
	st.pop()

	
10
9
8
7
6
5
4
3
2
1
>>> st
[]
>>> ## Q5)
>>> st = []
>>> for i in range(10):
	st.append(1+i)
>>> for i in range(10):
	st.pop(0)

	
1
2
3
4
5
6
7
8
9
10
>>> st
[]
>>> ## Q6)
>>> st = [1,2]
>>> st[2:] = [3,4,5]
>>> st
[1, 2, 3, 4, 5]
>>> 
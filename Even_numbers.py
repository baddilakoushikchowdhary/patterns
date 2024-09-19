num=2
for row in range(4):
	for col in range(4):
		if row==0 or row==3 or col==0 or col==2:
			print(num,end="		")
			num+=1
		else:
			print(end="	")
	print()

'''outout:-
1               2               3               4
5                       6
7                       8
9               10              11              12
'''
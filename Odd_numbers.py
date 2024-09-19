num=1
for row in range(4):
	for col in range(4):
		if row==0 or row==3 or col==0 or col==3:
			print(num,end="	")
			num+=2
		else:
			print(end="	")
	print()

'''output:-
1       3       5       7
9                       11
13                      15
17      19      21      23

'''
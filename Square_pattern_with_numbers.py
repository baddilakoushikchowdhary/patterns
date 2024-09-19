num=1
for row in range(3):
	for col in range(3):
		if row==0 or row==2 or col==0 or col==2:
			print(num,end="		")
			num+=1
		else:
			print(end="	")
	print()

'''output:-
1               2               3
4                               5
6               7               8
'''
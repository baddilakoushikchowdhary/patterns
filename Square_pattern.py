for row in range(4):
	for col in range(4):
		if row==0 or row==3 or col==0 or col==3:
			print("*",end="	")
		else:
			print(end="	")
	print()

'''output:-
*       *       *       *
*                       *
*                       *
*       *       *       *
'''
for row in range(5):
	for col in range(3):
		if row-col==2 or row+col==2 or col==0:
			print("*",end="    ")
		else:
			print(end="    ")
		
	print()
	print()

'''output:-
*        *

*    *

*

*    *

*        *

'''

for row in range(5):
	for col in range(5-row):
		print("*",end="  ")
	print()
	print(end=" "*(row+1))

'''output:-
*  *  *  *  *
 *  *  *  *
  *  *  *
   *  *
    *
'''
	
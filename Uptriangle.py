for row in range(5):
	print(end="  "*(4-row))
	for col in range(row+1):
		print("*",end="   ")
	print()

'''output:-
        *
      *   *
    *   *   *
  *   *   *   *
*   *   *   *   *
'''
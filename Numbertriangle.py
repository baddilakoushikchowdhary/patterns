temp=1
for row in range(5):
	print(end="  "*(4-row))
	for col in range(row+1):
		print(temp,end="   ")
	temp=temp+1
	print()
'''output:-
        1
      2   2
    3   3   3
  4   4   4   4
5   5   5   5   5
'''
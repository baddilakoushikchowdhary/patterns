given=input("enter the string:")
leng=len(given)
for row in range(leng):
	for col in range(row+1):
		print(given[col],end="  ")
	print()

'''output:-
enter the string:koushik
k
k  o
k  o  u
k  o  u  s
k  o  u  s  h
k  o  u  s  h  i
k  o  u  s  h  i  k
'''
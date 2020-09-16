def Feibonaqie(n):
	if n == 1 or n == 2:
		return 1
	if n >=3 :
		return (Feibonaqie(n-1) + Feibonaqie(n-2))


for i in range(1,10):
	print(Feibonaqie(i))
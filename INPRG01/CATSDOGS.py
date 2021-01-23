T = int(input())
for j in range(T) :
	C, D, L = map(int, input().split())
	if L % 4 != 0 :
		print("no")

	elif 2*D >= C :
		if L >= 4*D and L <= 4*(D + C) :
			print("yes")
		else :
			print("no")

	elif 2*D < C :
		if L >= 4*(C - D) and L <= 4*(D + C):
			print("yes")
		else :
			print("no")



#use min() function for optimisation
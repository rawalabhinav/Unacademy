R = int(input())
for i in range(R) :
	
	l = int(input())
	s = input()
	b = 0
	a = []
	for j in s :
		if j == "H" or j == "T" :
			a.append(j)  
	#List get's completed.
	while len(a) > 2*b :
		if len(a) % 2 != 0 :
			print("Invalid")
			break			

		elif a[2*b] == "H" and a[2*b + 1] == "T" :
			b = b + 1

		else :
			print("Invalid")
			break

	if 2*b == len(a) :
		print("Valid")








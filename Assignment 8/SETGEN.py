from itertools import combinations
for test in range(int(input())) :
	n = int(input())
	numbers = [i for i in range(1,n+1)]
	a = []
	for i in range(1,n+1):
		b = [sorted(i, reverse = True) for i in combinations(numbers,i)]
		a += sorted(b)
	print("")
	for i in sorted(a) :
		for j in sorted(i):
			print(j, end=" ")
		print("")
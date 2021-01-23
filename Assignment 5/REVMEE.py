n = int(input())
x = [int(x) for x in input().split()]
for i in range(len(x) - 1, -1, -1) :
	print(x[i], end=" ")
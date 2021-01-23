n = int(input())
x = [int(x) for x in input().split()]
x.reverse()
for i in range(len(x)) :
	print(x[i], end=" ")
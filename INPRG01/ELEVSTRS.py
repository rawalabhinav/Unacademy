T = int(input())
for i in range(T) :
	N, V1, V2 = map(int, input().split())
	if 2*(V1**2) >= V2**2 :
		print("Stairs")
	else :
		print("Elevator")

T = int(input())
for a in range(T) :
	N , H, Y1, Y2, L = map(int, input().split())
	i = 0
	for b in range(N) :
		t, x = map(int, input().split())
		if t == 1 :
			if H - Y1 > x: 
				L = L - 1				
		elif t ==2 :
			if Y2 < x :
				L = L - 1
		i = i + 1				
		if L == 0 :
			print(i - 1)
			break
	if L != 0 :
		print(i)

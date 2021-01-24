n, k = map(int, input().split())
x = [ int(x) for x in input().split()]
if x.count(k) != 0 :
	print(1)
else :
	print(-1)
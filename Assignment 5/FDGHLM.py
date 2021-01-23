a,b = map(int, input().split())
x = min(a,b)
y = max(a,b)
r = y%x
while r != 0 :
	y = x
	x = r
	r = y%x
print(x, (a*b)//x)

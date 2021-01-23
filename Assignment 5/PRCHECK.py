n = int(input())
cnt = 0
i = 1
while i**2 <= n:
	if n % i == 0 :
		cnt += 1
	i += 1
if cnt == 1 and n!= 1 :
	print(1)
else :
	print(0)
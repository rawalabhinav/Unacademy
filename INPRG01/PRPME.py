n = int(input())
p = 2
cnt = 0
while cnt < n :
	i = 1
	j = 0
	while i*i <= p :
		if p%i == 0 :
			j += 1
		i += 1
	if j == 1:
		print(p, end=" ")
		cnt = cnt + 1
	p += 1

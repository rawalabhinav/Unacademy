n = int(input())
isum = int(input())
tsum = 0
for i in range(n-1) :
	num = int(input())
	tsum += num*isum
	isum += num
print(2)
print(tsum)
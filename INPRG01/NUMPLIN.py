N = int(input())
n = N
sum = 0
while n != 0:
	sum = sum*10 + n%10 
	n = n//10
if sum == N :
	print("YES")
else :
	print("NO")

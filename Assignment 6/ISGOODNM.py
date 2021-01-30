n = int(input())
sum, i = 0, 2
while i**2 <= n :
    if n%i == 0 :
        sum += i + n//i
    i += 1
if n != 1 :
    sum += 1
if i**2 == n :
    sum += sum - i 
if sum == n :
    print("YES")
else:
    print("NO")

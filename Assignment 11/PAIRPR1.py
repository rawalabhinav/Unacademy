from itertools import combinations
def primecheck(x) :
    i = 2 
    while i*i <= x :
        if x%i == 0 :
            return False
        i+= 1
    return True

def primelist(n) :
    arr = [2]
    for i in range(3,n) :
        if i%2 == 0 : 
            pass
        elif primecheck(i) : 
            arr.append(i)
    return arr
        
for test in range(int(input())) :
    n = int(input())
    if n <= 3: 
        print(-1, -1)
        continue
    arr = primelist(n)
    condition = False
    if n%2 == 0 :
        for number in arr :
            if 2*number == n :
                print(number,number)
                condition = True
                break            
    if condition : continue
    found = False
    for primes in combinations(arr,2) :
        x,y = primes
        if x+y == n :
            print(x,y)
            found = True
            break
    if not found : print(-1, -1)
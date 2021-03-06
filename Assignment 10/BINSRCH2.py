import sys

def find_pos(x):
    print('1 ' + str(x))
    sys.stdout.flush()
    t = int(input())
    return t
    
def right(n, x):
    start = 0
    end = n
    while start < end:
        mid = (start+end)//2        
        if x < find_pos(mid): end = mid
        else: start = mid+1
    return start

def left(n, x):
    start = 0
    end = n
    while start < end:
        mid = (start+end)//2
        if find_pos(mid) < x: start = mid+1
        else: end = mid
    return start

def count(n, x):       
    return  right(n,x) - left(n,x) 

n = int(input())
x = int(input())
 
print('2 ' + str(count(n, x)))
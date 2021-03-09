import sys

def add(a, b):
    print('1', a, b) 
    sys.stdout.flush()
    return int(input())

def mul(res,a):
    var = res
    for j in range(a-1):
        res = add(res, var)
    return res

def pwr(a, b):
    res = 1
    # (a**b)modm = ((a**(b-1))modm*amodm)modm
    for i in range(b) :
        res = mul(res,a)

    return res


a, b = map(int, input().split())
ans = pwr(a, b)
print('2', ans)
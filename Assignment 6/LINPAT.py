def f(x) :
    if x%2 != 0:
        return 10*((x+1)//2)
    else :
        return x
for i in range(1,int(input())+1) :
    print(f(i), end=" ")
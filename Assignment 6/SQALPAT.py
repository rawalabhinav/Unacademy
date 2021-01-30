def line(x) :
    if x%2 == 0 :
        for i in range(5*x, 5*x -5,-1) :
            print(i, end=" ")
    else :
        for i in range(5*x -4,5*x +1) :
            print(i, end=" ")
n = int(input())
for x in range(1,n +1) :
    line(x)
    print("")
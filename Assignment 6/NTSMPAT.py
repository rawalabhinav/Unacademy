for i in range(1, int(input())+1) :
    for j in range(i, 2*i) :
        print(j, end=" ")
    for j in range(2*i -2, i - 1, -1) :
        print(j, end=" ")
    print("")
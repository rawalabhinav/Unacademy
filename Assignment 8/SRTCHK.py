for test in range(int(input())) :
    n = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    if sorted(A) == B :
        print("yes")
    else :
        print("no")
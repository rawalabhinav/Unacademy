for i in range(int(input())):
    (N ,H ,Y1 ,Y2 ,L)= map(int,input().split())
    cnt = 0
    for i in range(N):
        (t ,x)=map(int,input().split())
        if t == 1 and x >= H - Y1 and L > 0:
            cnt = cnt + 1
        elif t == 1 and x < H - Y1 and L >= 1:
            L = L - 1
            if L == 0:
                pass
            else:
                cnt = cnt + 1
        elif t == 2 and x <= Y2 and L > 0:
            cnt = cnt + 1
        elif t == 2 and x > Y2 and L >= 1:
            L = L - 1
            if L == 0:
                pass
            else:
                cnt = cnt + 1
    print(cnt)
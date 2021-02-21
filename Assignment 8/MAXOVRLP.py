def maxoverlap(start, end, n):
    ongoingclasses, intersectmax = 1,1
    i,j = 1,0
    while i < n and j < n:
        if start[i] > end[j]:     
            ongoingclasses -= 1
            j += 1    
        else:
            ongoingclasses += 1
            if ongoingclasses > intersectmax:         
                intersectmax = ongoingclasses                
            i += 1                
    print(intersectmax)

for test in range(int(input())) :
    n = int(input())
    m = int(input())
    start, end = [], []       
    for i in range(n) :
        l,r = map(int, input().split())
        start.append(l)
        end.append(r)
    maxoverlap(sorted(start),sorted(end),n)
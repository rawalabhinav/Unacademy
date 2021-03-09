def ans(matrix,transpose) :
    def lower(matrix) :
        for r in range(1,n) :
            for j in range(r,):
                row = matrix[r]
                element = row[j]
                if element != 0 :
                    return False
        return True
    def upper(matrix) :
        for r in range(n-1) :
            for j in range(r+1,n) :
                row = matrix[r]
                element = row[j]
                if element != 0 :
                    return False
        return True
    def diagonal(matrix) :
        for i in range(n) :
            if matrix[i][i] == 0 : return False
        return True


    def symmetric(matrix,transpose) :
        return matrix == transpose

    u, l, d = upper(matrix), lower(matrix), diagonal(matrix)

    if u and l:
        if d: return 7
        else :return 2
    elif u or l : return 2
    elif symmetric(matrix,transpose) : return 1
    else : return 0


for test in range(int(input())) :
    n = int(input())
    matrix = []
    transpose = [[] for i in range(n)]

    for i in range(n) :
        row = list(map(int, input().split()))
        matrix.append(row)
        for j in range(n) : 
            transpose[j].append(row[j])
    print(ans(matrix, transpose))
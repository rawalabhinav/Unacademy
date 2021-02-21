words = {}
matrix = []
rows, columns = {},{}
n,m = map(int, input().split())

#Task1 - Linking lengths with starting co-ordinates in crossword

for r in range(n) :
    line = list(input())
    matrix.append(line)
    temp = []    
    for index in range(m) :
        char = line[index]
        if char == "b" or char == "r" :
            temp.append(index)
    if len(temp) != 0 :
        rows[temp[1] -temp[0] +1] = [r,temp[0]]

for c in range(m) :
    temp = []
    for index in range(n) :
        row = matrix[index]
        char = row[c]
        if char == "b" or char == "c" :
            temp.append(index)
    if len(temp) != 0 :
        columns[temp[1] -temp[0] +1] = [temp[0],c]

for i in range(int(input())) :
    word = input()
    words[len(word)] = word

#Task2 - Primary Check

lengths = set(rows.keys()) | set(columns.keys())
if lengths != set(words.keys()) :
    print("Invalid")    
    exit()

#Task3 - Matrix Updation with secondary check

matrix = [["#"]*m for i in range(n)]

for length in rows.keys() :
    rc = rows[length]
    c = rc[1]
    row = matrix[rc[0]]
    word = words[length]
    i = 0
    for index in range(c,c +length) :
        row[index] = word[i]        
        i +=1

for length in columns.keys() :
    rc = columns[length]
    r = rc[0]
    row = matrix[rc[0]]
    c = rc[1]
    word = words[length]
    i = 0
    for index in range(r,r +length) :
        row = matrix[index]
        char = row[c]
        if char != "#" :
            if char != word[i] :
                print("Invalid")
                exit()
        row[c] = word[i]
        i +=1

for row in matrix :
    line = ''.join(row)
    print(line)
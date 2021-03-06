def choose_pivot(arr):
    database,indices = {},[]
    for index in range(len(arr)):
    	x,y = arr[index]
    	if x not in database.keys() : database[x] = index
    return sorted(database.values()) 

n = int(input())
arr_strip = list(map(int, input().split()))
arr = []
for i in range(0, 2*n, 2):
    arr.append((arr_strip[i], arr_strip[i+1]))

candidates = choose_pivot(arr)

print(len(candidates))
print(*candidates)
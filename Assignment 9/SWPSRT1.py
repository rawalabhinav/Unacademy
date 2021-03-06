def search(arr,start):
	index = start	
	for i in range(start +1, len(arr)) :
		if arr[index] > arr[i] :
			index = i
	return index

n = int(input())
arr = list(map(int, input().split()))
n, swaps = len(arr),0
indices = []
for i in range(n-1):
	j = search(arr,i)
	if i!=j :
		indices.append([i,j])
		arr[i],arr[j] = arr[j],arr[i]
		swaps += 1
print(swaps)
for pos in indices :	
	print(pos[0], pos[1])
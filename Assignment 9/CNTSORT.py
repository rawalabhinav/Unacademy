def countingsort(arr) :
	m = max(arr)
	#freq will have m +1 elements (done to link values with index)
	freq = [0]*(m+1)
	#calculating frequency
	for num in arr :
		freq[num] += 1
	#calculating cumulative frequency
	for i in range(m) : 
		freq[i+1] += freq[i]
	output = [0]*(len(arr))
	#filling the elements
	for k in range(len(arr)-1,-1,-1) :
		index = freq[arr[k]] - 1
		output[index] = arr[k]
		freq[arr[k]] -= 1
	return output

for test in range(int(input())) :
    n = int(input())
    arr = list(map(int, input().split()))
    for num in countingsort(arr) :
        print(num, end=" ")
    print('')
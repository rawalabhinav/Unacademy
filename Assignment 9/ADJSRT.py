def insertionsort(arr):
	swaps, result = 0,[]
    for i in range(1,len(arr)):
        j=i-1
        element = arr[i]
        while j >= 0 and element < arr[j]:
            arr[j+1]=arr[j]
            result.append(j)
            #equivalent to swap
            j-=1
        arr[j+1]= element
    return result

n= int(input())
arr = list(map(int,input().split()))
result = insertionsort(arr)
print(len(result))
for i in result: print(i,end=' ')
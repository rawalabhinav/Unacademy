def profit(arr):
    if len(arr) == 2:
        if arr[0] != arr[1]:
            return 1
        else:
            return 0
    mid = len(arr)//2
    left = profit(arr[:mid])
    right = profit(arr[mid:])
    L = set(arr[:mid])
    R = set(arr[mid:])
    if L&R: 
    	return left + right
    else :
    	return left + right +1

n = int(input())
provinces = list(map(int, input().split()))
print(profit(provinces))
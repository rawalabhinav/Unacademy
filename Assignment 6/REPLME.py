arr = []
for i in range(int(input())) :
    arr.append(int(input()))
if len(arr) == 1 :
    exit()
while len(arr) != 1 :        
    x,y = min(arr[0],arr[1]), max(arr[0],arr[1])
    z = (3*x +2*y)%100
    arr.pop(0), arr.pop(0)        
    arr.append(z) 
print(z)   

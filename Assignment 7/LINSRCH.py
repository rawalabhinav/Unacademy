a = []
for i in range(int(input())) :
    a.append(int(input()))
print(1)
for i in range(int(input())):
    if int(input()) in set(a) :
        print("yes")
    else :
        print("no")
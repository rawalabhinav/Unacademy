from math import ceil
entry,exit, plate = {},{},[]
for i in range(int(input())):
    activity = input().strip()
    number = input().strip()
    plate.append(number)
    t = int(input())
    if activity == "entry":
        entry[f"{number}"] = t
    else :
        exit[f"{number}"] = t
hours, amount = 0,0
for j in set(plate) :
    hours = ceil((exit[f"{j}"] - entry[f"{j}"])/60)
    amount += 60 + (hours -1)*30
print(amount)



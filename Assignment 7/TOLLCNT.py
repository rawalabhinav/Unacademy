from math import ceil
entry,exit, plate = {},{},[]
for i in range(int(input())):
    activity = input()
    number = input()    
    t = int(input())
    if activity == "entry":
        entry[number] = t
    else :
        exit[number] = t
hours, amount = 0,0
for j in entry.keys() :
    hours = ceil((exit[j] - entry[j])/60)
    amount += 60 + (hours -1)*30
print(amount)
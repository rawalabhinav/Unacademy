allpoints, allends = set(),set()
endpoints = {}

for segment in range(int(input())) :
    a,b,name,d = input().split()
    allpoints.add(a),allpoints.add(b)
    if name in endpoints :
        start,end = endpoints[name]
        if d == "E" or d == "S" :
            if start == b:
                endpoints[name][0] = a
            else :
                endpoints[name][-1] = b
        elif start == a :
            endpoints[name][0] = b
        else :
            endpoints[name][-1] = a
    else :
        if d == "E" or d == "S" :
            endpoints[name] = [a,b]
        else :
            endpoints[name] = [b,a]

for ends in endpoints.values() : 
    allends.update(ends)
print(len(allpoints - allends))
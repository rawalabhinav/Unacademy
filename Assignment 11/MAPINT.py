endsh, endsv = {}, {}
horizontal,vertical = set(),set()

for segment in range(int(input())) :
    a,b,name,d = input().split()

    if name in endsh.keys()  :
        horizontal.update([a,b])
        start, end = endsh[name]
        if d == "E" :
            if start == b:
                endsh[name][0] = a
            else :
                endsh[name][-1] = b
        elif start == a :
            endsh[name][0] = b
        else :
            endsh[name][-1] = a

    elif name in endsv.keys()  :
        vertical.update([a,b])
        start, end = endsv[name]
        if d == "S" :
            if start == b:
                endsv[name][0] = a
            else :
                endsv[name][-1] = b
        elif start == a :
            endsv[name][0] = b
        else :
            endsv[name][-1] = a
    else :
        if d == "E" : 
            horizontal.update([a,b])
            endsh[name] = [a,b]
        elif d == "W" : 
            horizontal.update([a,b])
            endsh[name] = [b,a]
        elif d == "S" : 
            vertical.update([a,b])
            endsv[name] = [a,b]
        else : 
            vertical.update([a,b])
            endsv[name] = [b,a]

temph,tempv = set(),set()
for ends in endsh.values() : temph.update(ends)
for ends in endsv.values() : tempv.update(ends)
horizontal -= temph
vertical -= tempv

print(len(horizontal&vertical))

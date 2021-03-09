for test in range(int(input())) :
    x, y, endx, endy = map(int, input().split())

    string = ""

    if endx >= x :
        string += "E"*(endx - x)

    else: 
        string += "W"*(x - endx)

    if endy >= y : 
        string += "N"*(endy - y)

    else : 
        string += "S"*(y - endy)

    print(len(string))
    print(string)
def filtered(x) :
    ans = x[0]
    cnt, negcase = 0,[]
    min = 10**9 +1
    for fraction in x:
        p,q = fraction
        if p <0 and q<0 :
            cnt += 1
    if cnt != len(x):
        for fraction in x :
            p,q = fraction
            if min > abs(p) and (not(p<0 and q<0)) :
                ans = fraction
                min = abs(p)
    else :
        for fraction in x :
            p,q = fraction
            if min > abs(p) :
                ans = fraction
                min = abs(p)
        return ans
    min = 10**9 +1
    for i in range(len(x)):
        fraction = x[i]
        p,q = fraction
        if p <0 and q>0 :            
            if min > abs(p) :
                min = abs(p)
                negcase = fraction
    if len(negcase) != 0:
        return negcase
    return ans

def get_distinct_fractions(arr):
    link,final = {},[]
    neginf,posinf = [],[]
    for pair in arr :
        p,q = pair
        if q == 0 :
            if p>0 : posinf.append(pair)
            else : neginf.append(pair)
        else :
            value = p/q
            if value in link.keys() : link[value] += [pair]
            else :  link[value] = [pair]
    distinct = sorted(link.keys())
    if len(neginf) != 0 :
        final.append(filtered(neginf))
    for value in distinct :
        final.append(filtered(link[value]))
    if len(posinf) != 0 :
        final.append(filtered(posinf))
    return final

n = int(input())
arr_strip = list(map(int, input().split()))
arr = []
for i in range(0, 2*n, 2):
    arr.append((arr_strip[i], arr_strip[i+1]))

result = get_distinct_fractions(arr)
print(len(result))
for x in result:
    print(x[0], x[1], end = ' ')

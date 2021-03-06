n = int(input())
for i in range(n) :
    print(n, end=" ")

'''
In the function lessthan(x<y)
it's checking if x is strictly less than y,
as there will be no such element we'd get exactly n(n-1)/2
comparisons.

Answer to bonus problem:

Had it been x<=y and saved any one of the repeating pivot
at the end (which we'd deal after the last comparison)
it'd be less likely to hit near n(n-1)/2 or the worst case will
never be hit atleast.
comparisons.
'''
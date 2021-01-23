A = int(input())
B = int(input())
C = int(input())
if A>B and A>C :
	if B>C :
		print(B)
	else :
		print(C)
elif B>C :
	if C>A :
		print(C)
	else :
		print(A)
elif B>A :
	print(B)
else :
	print(A)




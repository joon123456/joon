A = input()
A=A.lstrip()
A=A.rstrip()
if A == (''):
 print(0)
else:
 print(A.count(' ') + 1)

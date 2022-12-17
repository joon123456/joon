X=int(input())
N=int(input())
c=0
for i in range(N):
  a,b=input().split()
  a=int(a)
  b=int(b)
  c=c+a*b
if c==X:
 print("Yes")
else:
  print("No")

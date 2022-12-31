a,b=input().split()
a=int(a)
b=int(b)
if (a+b)%2==0 and b<=a and (a-b)%2==0:
 print(int((a+b)/2), int((a-b)/2))
else:
  print(-1)

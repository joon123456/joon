a=int(input())
b=int(input())
c=int(input())
if a<b and b<c:
  print(b)
if c<b and b<a:
  print(b)
if b<c and c<a:
  print(c)
if a<c and c<b:
  print(c)
if c<a and a<b:
  print(a)
if b<a and a<c:
  print(a)

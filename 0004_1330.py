A,B=input().split()
A=int(A)
B=int(B)
if (A>B) and (-10000<=A) and (B<=10000):
  print(">")
if (A<B) and (-10000<=A) and (B<=10000):
  print("<")
if (A==B) and (-10000<=A) and (B<=10000):
  print("==")

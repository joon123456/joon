a,b,c=input().split()
a=int(a)
b=int(b)
c=int(c)
if a>b>c:
 print(str(c) + " " + str(b) + " " +str(a))
elif a>c>b:
 print(str(b) + " " + str(c) + " " + str(a))
elif b>c>a:
 print(str(a) + " " + str(c) + " " + str(b))
elif b>a>c:
 print(str(c) + " " + str(a) + " " + str(b))
elif c>a>b:
 print(str(b) + " " + str(a) + " " + str(c))
elif c>b>a:
 print(str(a) + " " + str(b) + " " + str(c))

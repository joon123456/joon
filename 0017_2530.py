a,b,c=input().split()
a=int(a)
b=int(b)
c=int(c)
d=int(input())
p=[ ]
if int(c+(d%3600)%60)>=60:
  p.append(int(c+(d%3600)%60-60))
  b=b+1
else:
  p.append(int(c+(d%3600)%60))
if b+(d%3600)/60>=60:
  p.append(int(b+(d%3600)/60-60))
  a=a+1
else:
 p.append(int(b+(d%3600)/60))
d=(int(d/3600))
a=(a+d)%24
p.append(int(a)) 
print(p[2], p[1], p[0])

#A/3600 -> 시 
#(A%3600)/60 -> 분 
#(A%3600)%60 -> 초

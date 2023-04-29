def ver(a,b,c,d,e):
  return((a*a+b*b+c*c+d*d+e*e)%10)
a,b,c,d,e,= map(int,input().split())
print(ver(a,b,c,d,e))

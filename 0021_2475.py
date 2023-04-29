def ver(a,b,c,d,e):
  return((a*a+b*b+c*c+d*d+e*e)%10)
a,b,c,d,e,= map(int,input().split())
print(ver(a,b,c,d,e))

#or

def ver(data):
  sum = 0
  for i in data:
    sum = sum + i * i
  return (sum%10)

data = list(map(int, input().split()))
print(ver(data))

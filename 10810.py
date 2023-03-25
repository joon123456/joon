n,m = map(int,input().split())

arr = [0 for i in range(101)]

for i in range (m) :
  st,ed,val = map(int,input().split())
  for j in range(st,ed+1) :
    arr[j] = val

for i in range(1,n+1) :
 print(arr[i],end=' ')


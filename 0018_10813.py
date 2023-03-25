n,m = map(int,input().split())

arr = [i for i in range(101)]

for i in range (m) :
  pos1, pos2 = map(int,input().split())
  arr[pos1] , arr[pos2] = arr[pos2] , arr[pos1]


for i in range(1,n+1) :
 print(arr[i],end=' ')

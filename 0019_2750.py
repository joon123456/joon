n = int(input())
arr = []
sarr = []
for i in range(n):
  arr.append(int(input()))
  inx=0
  for j in range(len(sarr)):
     if sarr[j]<arr[i]:
      inx += 1
  sarr.insert(inx,arr[i])
for i in range(n) :
 print(sarr[i])



           

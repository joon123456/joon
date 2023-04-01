n = 5
arr = []
sarr = []
for i in range(n):
  arr.append(int(input()))
  inx=0
  for j in range(len(sarr)):
     if sarr[j]<arr[i]:
      inx += 1
  sarr.insert(inx,arr[i])
print(int(arr[0]/5+arr[1]/5+arr[2]/5+arr[3]/5+arr[4]/5))
print(sarr[2])

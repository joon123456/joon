a=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30 ]
for i in range(1,29):
  b=int(input())
  a.remove(b)
print(a[0])
print(a[1])



#or


student = list(range(1,31))
for i in range(28):
  solved = int(input())
  student.remove(solved)

print(student[0])
print(student[1])

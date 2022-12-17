M,N=input().split()
N=int(N)
M=int(M)
Joon = []
Joon2 = []
for i in range(M):
  c = list(map(int,input().split()))
  Joon.append(c)
for i in range(M):
  c = list(map(int,input().split()))
  Joon2.append(c)
Joon3 = []
for i in range(M):
  Joon4 = []
  for j in range(N):
     Joon4.append(Joon[i][j] + Joon2[i][j])
  Joon3.append(Joon4)
for i in range(M):
  for j in range(N):
    print(Joon3[i][j],end = ' ') 
  print()
  
  




  
  







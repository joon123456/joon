def operator(A,B):
  return (A+B)*(A-B)
A,B = map(int, input().split())
print(operator(A,B))

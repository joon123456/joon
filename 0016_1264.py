c = ["a","e","i","o","u","A","E","I","O","U"]
while true:
  a=input()
  if a == '#':
   break
  b=0
  for c in a:
    if c in "aeiouAEIOU": 
     b=b+1
  print(b)

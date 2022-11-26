a=input()
b = ''
for i in a:
  if i.isupper():
     b=b+i.lower()
  else:
     b=b
  if i.islower():
     b=b+i.upper()
  else:
     b=b
  
print(b)

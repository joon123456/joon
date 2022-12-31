while True:
 a=input()
 if a=="END":
  break
 for i in range(len(a)):
    print(a[-i-1], end = "")
 print()
 

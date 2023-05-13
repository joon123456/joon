a=input()
if a=="A+":
 print("4.3")
elif a=="A0":
 print("4.0")
elif a=="A-":
 print("3.7")
elif a=="B+":
 print("3.3")
elif a=="B0":
 print("3.0")
elif a=="B-":
 print("2.7")
elif a=="C+":
 print("2.3")
elif a=="C0":
 print("2.0")
elif a=="C-":
 print("1.7")
elif a=="D+":
 print("1.3")
elif a=="D0":
 print("1.0")
elif a=="D-":
 print("0.7")
elif a=="F":
 print("0.0")
 
 
 #or
 
 M=input() + "0"
b=0.0
if M[0]=="A":
  b=b+4.0
elif M[0]=="B":
  b=b+3
elif M[0]=="C":
  b=b+2
elif M[0]=="D":
  b=b+1
elif M[0]=="F":
  b=b

if M[1]=="+":
  b=b+0.3
elif M[1]=="0":
  b=b
elif M[1]=="-":
  b=b-0.3
elif m[1]=="":
  b=b

print(b)
  
  

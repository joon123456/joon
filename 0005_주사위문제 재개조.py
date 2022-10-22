import random

def game(a,b,c):
  if (a == b == c): 
     return (10000 + a* 1000)

  elif a == b:
      return (1000 + a* 100)

  elif b == c:
      return (1000 + b* 100)

  elif c == a:
      return (1000 + c* 100)


  elif (a > b > c):
      return (a * 100)

  elif (a > c > b):
      return (a * 100)

  elif (b > a > c):
      return (b * 100)

  elif (b > c > a):
      return (b * 100)

  elif (c > a > b):
      return (c * 100)

  elif (c > b > a):
      return (c * 100)


while True:

  name1 = input('a플레이어의 이름을 입력하시오(-1은 종료)\n')

  if(name1 == '-1'):
   break

  a1 = random.randrange(1,7)
  b1 = random.randrange(1,7)
  c1 = random.randrange(1,7)
  score1 = game(a1,b1,c1)

  name2 = input('b플레이어의 이름을 입력하시오(-1은 종료)\n')

  if(name2 == '-1'):
   break

  a2 = random.randrange(1,7)
  b2 = random.randrange(1,7)
  c2 = random.randrange(1,7)
  score2 = game(a2,b2,c2)
   
  name3 = input('c플레이어의 이름을 입력하시오(-1은 종료)\n')

  if(name3 == '-1'):
   break

  a3 = random.randrange(1,7)
  b3 = random.randrange(1,7)
  c3 = random.randrange(1,7)
  score3 = game(a3,b3,c3)

  print(str(score1) + " vs " + str(score2) + " vs " + str(score3))

  if (score1 > score2 > score3) or (score1 > score3 > score2) or (score1 > score2 == score3):
   print(name1 + "의 승리\n")
  
  elif(score2 > score1 > score3) or (score2 > score3 > score1) or (score2 > score1 == score3):
   print(name2 + "의 승리\n")

  elif(score3 > score1 > score2) or (score3 > score2 > score1) or (score3 > score1 == score2):
    print(name3 + "의 승리\n")
  
  else:
   print("비김\n")

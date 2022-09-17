import random # 시작을 하기전에 미리 다른 사람의 라이브러리를 사용했다고 선언한다.

def game(a,b,c): # 일종의 함수로, 자신이 자주 사용하는것을 모아놓음.
  if (a == b == c): # a 와 b 와 c 가 모두 같을때
     return (10000 + a* 1000) # 10000+a(1000)값을 return(함수에서 쓰임. 함수에서 넣은 값을 돌려받는다는 뜻. 결과)한다. (print를 쓰면 함수 score을 비교할 수 없게됨.)

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


while True: #반복문. (While 과 for 문으로 나뉨) While: (물결표) 인동안에.  For: While과 다르게 한문장을 나눠 좀더 세세하게 표현.

  name1 = input('a플레이어의 이름을 입력하시오(-1은 종료)\n') #name1 의 이름을 구한다

  if(name1 == '-1'): #만약 name1이 -1이된다면
   break #즉시 종료한다

  a1 = random.randrange(1,7) # a1(주사위 이름)이 1이상 7미만의 범위에서 무작위로 하나를 고른다
  b1 = random.randrange(1,7) # b1(주사위 이름)이 1이상 7미만의 범위에서 무작위로 하나를 고른다
  c1 = random.randrange(1,7) # c1(주사위 이름)이 1이상 7미만의 범위에서 무작위로 하나를 고른다
  score1 = game(a1,b1,c1) # a1, b1, c1에서 나온값들을 이용해 score1을 구한다.

  name2 = input('b플레이어의 이름을 입력하시오(-1은 종료)\n') #name2 의 이름을 구한다

  if(name2 == '-1'): #만약 name2가 -1이된다면
   break #즉시 종료한다

  a2 = random.randrange(1,7) #a2(주사위 이름)이 1이상 7미만의 범위에서 무작위로 하나를 고른다
  b2 = random.randrange(1,7) #b2(주사위 이름)이 1이상 7미만의 범위에서 무작위로 하나를 고른다
  c2 = random.randrange(1,7) #c2(주사위 이름)이 1이상 7미만의 범위에서 무작위로 하나를 고른다
  score2 = game(a2,b2,c2) # a2, b2, c2에서 나온값들을 이용해 score2를 구한다.

  print(str(score1) + " vs " + str(score2)) # score1 과 score2의 값을 숫자->문자로 한다음 (score 1)vs(score2)를 출력한다

  if (score1 > score2): #만약 score1의 값이 score2의 값보다 크면
   print(name1 + "의 승리\n") # name 1의 이름을 말하고 뒤에 의 승리를 붙인것을 프린트한다 (\n은 한개 뛴다는뜻)

  elif(score2 > score1):
   print(name2 + "의 승리\n") #만약 score2의 값이 score1의 값보다 크면 # name 2의 이름을 말하고 뒤에 의 승리를 붙인것을 프린트한다 (\n은 한개 뛴다는뜻)

  else: #두 상황중 한개도 안나오면
   print("비김\n") #비김이라고 출력한다

def solution(n):
    c=[]
    for i in range(1,n+1):
        if n%i==0:
            c.append(i)
            c.sort()
    return c

#반복문을 만들어 1부터 n까지 가는 반복문 생성
#n 나누기 i를해서 정수인것들은(나머지가 0) 모두 n의 약수
#리스트 하나 생성
#리스트에 n의 약수 추가
#오름차순으로 정렬

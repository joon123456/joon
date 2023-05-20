def solution(a, b, n):
    cola = 0
    answer= 0
    while n>=a:
        cola = n//a*b
        answer = answer + cola
        n = n%a + cola
    return answer 

#빈병수에서 a로 나누고 b를 곱한다(빈병수로 인해 받게되는 병수)
#answer = answer + 빈병수//a*b
#빈병수로 인해 받게되는 병수를 모두 마시고 난후
#다시 빈병수를 a로 나누고 b를 곱한다(바꿔온 콜라 수)
#answer = answer + 빈병수//a*b + 빈병수//a*b
#보유중인 병수가 a개 미만일때까지 반복(while 문)
#바꿔온 콜라 수들을 모두 더하여 리턴

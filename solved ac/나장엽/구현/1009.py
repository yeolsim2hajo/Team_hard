import sys
input = sys.stdin.readline
T = int(input())

# 아래의 코드는 10 1 을 처리하지 못함
# for _ in range(T):
#     a, b = map(int, input().split())
#     data = a ** b # 데이터의 개수는 a^b
#     result = data % 10
#     print(result)


# 자연수의 연산 원리를 이해해야 풀 수 있음
# 344 * 129 를 연산했을때 마지막 자리의 수는 무엇일까? -> 간단하게 4 * 9 = 36, -> 마지막 자리수는 6
# 다른 숫자의 계산결과는 모두 10이상의 자리에서 계산이 된다 -> 컴퓨터가 10개라고 정해져있으므로 10의 자리 이상부터는 신경안써도 된다.
# but, 10 1의 경우  마지막 자릿수가 0으로 떨어진다. 이 경우에는 0번 컴퓨터가아닌, 10번 컴퓨터가 답이다. -> 조건 주기

import sys 
input = sys.stdin.readline

t = int(input())
for _ in range(t):
	a,b = map(int,input().split())
	aa=a%10

	if aa == 0: # 패턴 1
		print(10)
	elif aa in [1,5,6]: 
		print(aa)
	elif aa in [4,9]: #패턴 2
		bb=b%2
		if bb == 0:
			print(aa*aa%10)
		else:
			print(aa)
	else: #패턴 4
		bb=b%4  
		if bb ==0:
			print(aa**4%10)
		else:
			print(aa**bb%10)
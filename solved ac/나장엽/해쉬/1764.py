# import sys
# input = sys.stdin.readline


n, m = map(int, input().split())

no_see = set()
no_hear = set()

for i in range(n):
    no_see.add(input())
for k in range(m):
    no_hear.add(input())


answer = sorted(list(no_see & no_hear))

print(len(answer))
for i in range(len(answer)):
    print(answer[i])


#set함수는 집합 자료형
#교집합을 구하고 싶다면 & 사용
#합집합은 |
#차집합은 -, difference 함수 no_see.difference(no_hear)
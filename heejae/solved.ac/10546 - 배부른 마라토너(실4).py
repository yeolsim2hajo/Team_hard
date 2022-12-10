# start와 end의 각 수를 비교하여, 해당하는 이름의 value가 다르다면 그 사람이 완주 못한 사람이다.

import sys 

start = dict()
end = dict()
n = int(input())

for _ in range(n): # start dict채우기
    name = sys.stdin.readline().rstrip()
    if name in start:
        start[name] += 1 # 이미 있다면, 완주했을 수도 있다는 뜻(동명이인 가능성 열어두고) -> +1
    else:
        start[name] = 1 # 처음이라면, 1

for _ in range(n-1): # end dict채우기
    name = sys.stdin.readline().rstrip()
    if name in end:
        end[name] += 1
    else:
        end[name] = 1

# 완주를 하지 않은 한 명만 찾으면 바로 for문을 빠져나오면 된다.
for n in start.keys():
    if n not in end:
        print(n)
        break
    else: # 동명이인의 경우
        if start[n] != end[n]:
            print(n)
            break
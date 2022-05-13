# K, M = map(int, input().split())
# cables = []
# for i in range(K):
#     cables.append(int(input()))

# total = sum(cables)
# slice_cable = total//11

# cnt = 0
# while True:
#     if cnt >= M:
#         break

#     cnt = 0
#     for i in range(K):
#         cnt += cables[i] // slice_cable

#     if cnt < M:
#         slice_cable -= 1


# print(slice_cable)
## 시간초과.
## 반례 존재 
# 4 4
# 4
# 1
# 5
# 5

import sys

def solution():
    K, N = map(int, input().split())
    lan = [int(sys.stdin.readline()) for _ in range(K)] 
    # input() 내장 함수는 sys.stdin.readline()과 비교해서 prompt message를 출력하고, 개행 문자를 삭제한 값을 리턴하기 때문에 느리다.
    
    min_value = 1 # 랜선의 최소 길이를 1로 설정
    max_value = max(lan) # 랜선중 가장 긴 길이를 max값으로 설정

    while min_value <= max_value: # 이분탐색이 완료될때까지 반복
        mid = (min_value + max_value) // 2 # 이분탐색을 위한 중간값 설정
        cnt = 0 # 랜선 수를 카운팅하는 변수 반복될때 마다 초기화 해야 하므로 반복문 안에서 선언
        for i in lan:
            cnt += i // mid # 랜선을 자른 수

        if cnt >= N: # 랜선을 자른 수가 만들어야 될 랜선의 수보다 클 경우 
            min_value = mid + 1 # 랜선의 최소 길이를 중간값보다 1크게 설정
        else: # 랜선을 자른 수가 만들어야 될 랜선의 수보다 작을 경우 
            max_value = mid - 1 # 랜선의 최대 길이를 중간값보다 1작게 설정

    return max_value # 랜선을 자룬 수가 만들어야 될 랜선의 수와 같을경우 길이 출력

print(solution())
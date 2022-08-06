# 배열의 구간에서 원소를 일일이 훑으며 더해주는 것은 시간 복잡도가 O(N2)에 가깝게 된다고 한다
# 아래 코드가 딱 그 짝
# N, M = map(int,input().split())
# num_list = list(map(int,input().split()))

# for tc in range(M):
#     i, j = map(int,input().split())
#     print(sum(num_list[i-1:j]))

# 핵심: [5,4,3,2,1] / 2번째~4번째 구간합 구하기
    # way1: 4+3+2 => 로 총 3번 더해야한다. 그러나, 미리 구간합을 구해놓는다면
        # (( temp = [0,5,9,12,14,15] ))
        # way2: temp[4] - temp[1]  => 총 2번만 연산하면 된다
            # 지금은 체감이 안되지만,
            # 만약 M이 9999 / i가 1, j가 9998이라면 -> 총 9998번을 일일이 더해줘야 한다
            # 하지만 위 방법대로 하면, 마찬가지로 2번의 연산이면 해결된다

import sys
input = sys.stdin.readline # 이거 넣어줘야 통과.. -> 아니면 시간초과;;

N, M = map(int,input().split())
num_list = list(map(int,input().split()))

# 구간합 알고리즘이 따로 있었음 -> prefix sum
# 1. 구간합 구하기
accu = [0]
for k in range(N):
    accu.append(accu[-1]+num_list[k])

# 2. "j번"인덱스에서 "i-1번" 인덱스 빼주기 (연산 2번으로 해결)
for tc in range(M):
    i, j = map(int,input().split())
    print(accu[j]-accu[i-1])
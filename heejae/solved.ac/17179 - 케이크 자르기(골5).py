N, M, L = map(int, input().split())
sections = [int(input()) for _ in range(M)] + [L]

# 최소 여부를 체크하는 함수
def check(ele):
    left, cnt = 0, 0
    for right in sections: # 각 구간을 순회
        if right - left >= ele:
            left = right # 최대 오른쪽을 조건이 될때까지 찾고,
            cnt += 1
    if cnt > t: # cnt가 자르는 횟수(t)를 넘어선다면 true
        return True
    return False # 아니라면 false

for _ in range(N): # N: test case
    t = int(input())
    left = 1 # L크기 최소: 1
    right = 4000000 # L크기 최대: 4,000,000
    answer = 0
    # 모든 구간중에서, t개 선택 -> 가장 작은 조각 길이가 나올때까지 체크
    while left <= right: # 이분탐색 원리
        mid = (left + right) // 2
        if check(mid): # return true의 경우
            left = mid + 1
            answer = max(mid,answer) # 가장 작은 조각의 '최댓값'을 구하기 때문
        else: # return false의 경우 -> 즉, 아니라면 줄이기
            right = mid - 1
    print(answer)
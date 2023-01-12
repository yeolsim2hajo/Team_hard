#221020
from sys import stdin
from heapq import heapify, heappop
new_input = stdin.readline
N, M = map(int, new_input().split())
subject = []
for _ in range(N):
    P, L = map(int, new_input().split())
    mileage = list(map(int, new_input().split()))
    heapify(mileage)
    if P-L >= 0:
        for _ in range(P-L):
            heappop(mileage)
        subject.append(heappop(mileage))
    else:
        subject.append(1)
heapify(subject)

cnt = 0
for _ in range(N):
    M -= heappop(subject)
    if M >= 0:
        cnt += 1
    else:
        break
print(cnt)


# 함수 - 시간, 메모리 같음
def apply():
    from sys import stdin
    from heapq import heapify, heappop
    new_input = stdin.readline
    N, M = map(int, new_input().split())
    subject = []
    for _ in range(N):
        P, L = map(int, new_input().split())
        mileage = list(map(int, new_input().split()))
        heapify(mileage)
        if P - L >= 0:
            for _ in range(P - L):
                heappop(mileage)
            subject.append(heappop(mileage))
        else:
            subject.append(1)
    heapify(subject)

    cnt = 0
    for _ in range(N):
        M -= heappop(subject)
        if M >= 0:
            cnt += 1
        else:
            return cnt
    return cnt
print(apply())

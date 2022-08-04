#1495 기타리스트
N, S, M = map(int, input().split())
dif = list(map(int, input().split()))
def find_max():
    now = {S}
    next = set()
    for i in range(N):
        for volume in now:
            if 0 <= volume+dif[i] <= M:
                next.add(volume+dif[i])
            if 0 <= volume-dif[i] <= M:
                next.add(volume-dif[i])
        if next:
            now = set(next)
            next.clear()
        else:
            return -1
    return max(now)
print(find_max())

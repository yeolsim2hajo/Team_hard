#1966 프린터 큐
T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    documents = input().split()
    printed = [False] * N
    cnt = front = 0
    while True:
        idx = front%N
        if printed[idx]:
            front += 1
        else:
            for i in range(N):
                if printed[i] is False and documents[i] > documents[idx]:
                    front += 1
                    break
            else:
                cnt += 1
                if idx == M:
                    print(cnt)
                    break
                else:
                    printed[idx] = True
                    front += 1
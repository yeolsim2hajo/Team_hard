#221206
N, M = map(int, input().split())
numbers = [[] for _ in range(N)]
if M == 1:
    for i in range(N):
        print(*[i+1]*N)
elif M == 2:
    number_list = list(range(1, N+1))
    for i in range(N):
        if i%2:
            print(*number_list[::-1])
        else:
            print(*number_list)
else:
    for i in range(1, N+1):
        for j in range(1, N+1):
            print(i*j, end=' ')
        print()

import sys
new_input = sys.stdin.readline
T = int(new_input())
for _ in range(T):
    A, B = map(int, new_input().split())
    if B < A:
        A, B = B, A
    if A%2 or B%2:
        start, step = 3, 2
    else:
        start, step = 2, 2
    multiple = answer = A * B
    for i in range(start, A+1, step):
        if A%i == B%i == 0:
            answer = min(answer, multiple//i)
    print(answer)

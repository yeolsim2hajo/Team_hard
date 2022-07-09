import sys

read = lambda: sys.stdin.readline().rstrip()

L, R = read().split()

answer = 0

if len(L) != len(R):
    print(0)
else:
    for i in range(len(L)):
        if L[i] == R[i]:
            if L[i] == '8':
                answer += 1
        else:
            break

    print(answer)
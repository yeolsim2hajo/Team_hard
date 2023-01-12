#230106
N, M = map(int, input().split())
S = set(map(int, input().split()))
min_dif = 1e9
for i in range(1, 1001):
    if i not in S:
        if abs(i-N) < min_dif:
            for j in range(i, 1001):
                if j not in S:
                    two = i*j
                    if abs(two-N) < min_dif:
                        for k in range(j, 1001):
                            if k not in S:
                                dif = abs(N-two*k)
                                if dif < min_dif:
                                    min_dif = dif
                                else:
                                    break
                    else:
                        break
        else:
            break
print(min_dif)

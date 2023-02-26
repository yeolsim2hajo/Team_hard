#230226
def find_cnt(N):
    if N < 100:
        return N
    cnt = 99
    left = N//100
    for i in range(1, left):
        cnt += (9-i)//2 + i//2 + 1

    mid = (N%100)//10
    for j in range(mid):
        if 0 <= 2*j - left <= 9:
            cnt += 1

    max_num = 2*mid - left
    if 0 <= max_num <= 9 and max_num <= N%10:
        cnt += 1

    return cnt

N = int(input())
print(find_cnt(N))
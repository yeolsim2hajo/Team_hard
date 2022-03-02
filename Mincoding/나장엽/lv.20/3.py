# 마이클잭슨 무브먼트
# 3 5 4 6 2 9 를 입력받으면
# 3 5 4 6 2 9 2 6 4 5 3  이 출력된다


arr = list(map(int, input().split()))


def mic(level, idx):
    print(arr[idx], end = ' ')
    if level == 5:
        idx = idx - 1
        return idx

    mic(level + 1, idx + 1)
    print(arr[idx], end= ' ')


mic(0, 0)
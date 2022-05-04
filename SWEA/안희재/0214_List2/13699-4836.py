# 이거 행렬문제네..
# 버킷 2개 만들어서
# 서로 겹치는 개수 출력하면 될듯?
# 아 ㅆㅂ 꼭지점이네 기준이..
T = int(input())

for idx in range(1, T+1):
    bucket_1 = [[0] * 10 for _ in range(10)]
    bucket_2 = [[0] * 10 for _ in range(10)]

    num = int(input())
    for i in range(num):
        r1,c1,r2,c2, color = list(map(int,input().split()))
        if color == 1:
            for j in range(r1,r2+1):
                for k in range(c1,c2+1):
                    bucket_1[j][k] = 1
        else:
            for j in range(r1,r2+1):
                for k in range(c1,c2+1):
                    bucket_2[j][k] = 1

    cnt = 0
    for i in range(10):
        for j in range(10):
            if bucket_1[i][j] == bucket_2[i][j] == 1: # 이렇게 3개 써도 되네 조건을
                cnt += 1

    print(f'#{idx}', cnt)
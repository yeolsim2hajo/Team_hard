# 영현님 코드
T = int(input())

for t in range(1, T+1) :
    N = int(input())

    pascal = [ [1], [1,1] ]
    for i in range(2, N) :
        list = [1]
        for j in range(i-1) :
            list += [pascal[i-1][j] + pascal[i-1][j+1]]
        list += [1]
        pascal += [list]

    print("#{}".format(t))
    for i in range(N) :
        print(*pascal[i])

#  ㅆㅂ ㅠ 이렇게 간단하게 되네..
# 아직 그냥 내 구현력이 모자른듯..
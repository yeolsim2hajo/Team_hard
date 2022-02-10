a = int(input())

# 그리디 알고리즘 배운김에 써봤음
# 근데, 이 문제는 조작 불가의 경우 아래처럼 해도 되지만
# 이 코드가 범용적인 코드는 아닌 것 같음. 다른 방법 없나?
b = str(a)
if b[len(b)-1] != '0':
    print(-1)
else:
    coins = [300, 60, 10]
    result = [0, 0, 0]

    for idx in range(len(coins)):
        result[idx] = a // coins[idx]
        a = a % coins[idx]
    print(' '.join([str(x) for x in result]))

# 아래가 더 음.. 간단(?)하긴 하지
# N = int(input())

# if N % 10 != 0:
#     print(-1)
# else:
#     a = b = c = 0
#     a = (N//300)
#     b = (N%300) // 60
#     c = (N%60) // 10
#     print(a, b, c)
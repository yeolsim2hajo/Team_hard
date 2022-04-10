'''
이상한 369
13 16은 x
36 39는 ok
'''

# 3-> 1 6 -> 2 9 -> 3 / 33 -> 4? (1+3)  36 -> 5? (2+3) 39 -> 6 (3+3)? / 63 -> 7 (1+6)


def sol():
    num = list(input())
    clap = 0
    cnt = 1
    data = {'3': 1, '6': 2, '9': 3}

    for i in range(len(num)):
        clap += data[num.pop()] * cnt
        cnt *= 3

    return clap
print(sol())

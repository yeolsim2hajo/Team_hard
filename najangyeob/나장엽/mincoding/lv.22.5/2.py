# 나에게 호감을 갖고 있는 n명의 친구가 있음
# 누구와 데이트할 지 ox로 조합을 출력
# n을 입력받고 그에 따른 데이트 조합을 출력해라


n = int(input())
combi = ['']*n
signal = ['x','o']


def dating(level):
    global n
    if level == n:
        for i in range(n):
            print(combi[i], end='')
        print()
        return
    
    for i in range(2):
        combi[level] = signal[i]
        dating(level+1)

dating(0)
#221014
N = int(input())
cnt = 0
for _ in range(N):
    alp = {}
    word = input()
    pre = ''
    for element in word:
        if pre != element:
            if alp.get(element):
                break
            else:
                alp[element] = 1
                pre = element
    else:
        cnt += 1
print(cnt)


# 함수로
def find_cnt():
    N = int(input())
    cnt = 0
    for _ in range(N):
        alp = {}
        word = input()
        pre = ''
        for element in word:
            if pre != element:
                if alp.get(element):
                    break
                else:
                    alp[element] = 1
                    pre = element
        else:
            cnt += 1
    return cnt
print(find_cnt())
# 경사로는 낮은 칸에 놓으며, 높이차이 1이여야 함
# L = 2, -> 3 2 2 3 -> x
# L = 1, -> 3 2 2 1 2 3 -> x
# 순회하면서, 크기차이가 나면 경사로 ㄱㄱ
# 경사로 완성시키는 구간은 아예 lst에서 pop시키고, 새로 ㄱ

N, L = map(int,input().split())

def Check_Runway(lst, L): # lst, 경사로 길이가 인자
    for i in range(len(lst)-1):
        if abs(lst[i] - lst[i+1]) > 1: # 칸 높이가 2이상 차이나면 바로 false
            return 0 # 실패

    for i in range(len(lst)):
        if lst[i] > lst[i+1]: # 다음이 낮은 칸이면,
            tmp = lst[i+1]
            cnt = 0
            for j in range(i+1,len(lst)):
                if lst[j] == tmp:
                    cnt += 1
                else:
                    if cnt >= L:
                        continue








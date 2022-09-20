# 아 이번엔 path로 해보자.. 도찐개찐같긴한데..

T = int(input())
for tc in range(1,T+1):
    N = int(input())

    arr = [10,20,20]
    path = [''] * (N//10) # 최대개수는 N//10만큼. (10원짜리 동전으로만)
    cnt = 0

    def abc(level, sum):
        if sum > N:
            return
        if sum == N:
            global cnt
            cnt += 1
            return
        
        if level == (N//10)+1:
            return

        for i in range(3):
            path[level] = arr[i]
            abc(level+1, sum+arr[i])

    abc(0, 0) # level, sum = 0, 0
    print(f'#{tc}', cnt)

# ㅅㅂ 이것도 아니네.. 심지어 이건 8/10만 맞음..
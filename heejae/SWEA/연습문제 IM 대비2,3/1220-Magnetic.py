#1은 N극, 2는 S극 // 위쪽은 N극, 아래쪽은 S극
# 아 걍 괄호검사처럼, 1다음에 2? or 2다음에 1? 그거만 찾으면 될듯?

for tc in range(1,11):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(100)]
    cnt = 0

    for i in range(100):
        stack = '' # 이거 밖에다 썼음.......ㅜ
        for j in range(100):
            if arr[j][i] == 1:
                stack = 'N'
            if arr[j][i] == 2 and stack =='N':
                cnt += 1
                stack = ''

    print(f'#{tc}', cnt)

# 와 ㅈㄴ간단한 문제였네 ㅅ;ㅂ;;;

for tc in range(1,11):
    N, pw = input().split()
    pw = list(pw)
    N = int(N)

    while (1): # 언제까지? 계속 pop시킨 새 단어 반복문 돌릴때 같은게 발견되지 않으면
        for i in range(len(pw)-1):
            if pw[i] == pw[i+1]:
                pw = pw[0:i] + pw[i+2:] # 동일한, 연속된 구간만 삭제해줌
                break # 그리고, 멈추고 바뀐 새 단어로 다시 for문 돌리기
        else:
            break # 끝까지 돌렸는데도, break가 안걸리면 while문 종료

    print(f'#{tc}', ''.join(pw))

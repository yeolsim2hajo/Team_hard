# 그리디?
N = int(input()) # N은 정량 , 화물은 7/3

cnt = 0

cnt += N // 7
N -= 7 * cnt # N은 6이하로 떨어짐

while 1:
    if N % 3 == 0:
        cnt += N // 3
        print(cnt)
        break
    # 만약, 나누어떨어지지 않으면 일단 빼기
    N -= 3
    cnt += 1
    if N < 0: # 뺏는데, 음수가 되어버리면
        print(-1)
        break

# 아래처럼 하면 더 깔끔하네..
# ---------------------------------
# N = int(input())
# result = 0

# while True:
#     if N%7 ==0:
#         result += N//7
#         print(result)
#         break
#     N -= 3
#     result += 1
#     if N < 0:
#         print(-1)
#         break

# 아. 어차피, 3부터 찾아봐도 상관이 없구나
# point는 나누어떨어지지 않는다면 결국 break이므로
# 3을 계속 빼면서, 7의 배수가 될때까지 find

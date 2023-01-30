#230129
# 시간 초과
# N = int(input())
# cnt = 1
# if N > 1:
#     start = 2 if N%2 else 3
#     half = N//2
#     for length in range(start, half):
#         total = sum(range(1, 1+length))
#         end = N//length+2
#         for num in range(1, end):
#             if total == N:
#                 cnt += 1
#                 break
#             if total > N:
#                 break
#             total += length
# print(cnt)


#
N = int(input())
cnt = 1
if N > 1:
    half = N//2 + 1
    for i in range(2, half):
        i_half = i//2
            quot = N//i
        # 홀수 => 나눠 떨어져야
        if i%2:
            if N%i == 0:
                if 1 <= quot - i_half:
                    cnt += 1
        elif N%i == i//2:
            if :
                cnt += 1
print(cnt)

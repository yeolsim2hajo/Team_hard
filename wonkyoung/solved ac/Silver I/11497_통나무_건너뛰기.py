#221225
# from collections import deque
# T = int(input())
# for _ in range(T):
#     N = int(input())
#     log_list = sorted(map(int, input().split()))
#     final_list = deque()
#     dif = []
#     final_list.append(log_list.pop())
#     back = True
#     while log_list:
#         try:
#             final_list.append(log_list.pop())
#             final_list.appendleft(log_list.pop())
#         except Exception:
#             break
#     for i in range(N):
#         dif.append(abs(final_list[i] - final_list[i-1]))
#     print(max(dif))



# 함수
T = int(input())
def hopping():
    from collections import deque
    N = int(input())
    log_list = sorted(map(int, input().split()))
    final_list = deque()
    dif = []
    final_list.append(log_list.pop())
    for i in range(N-1, -1, -2):
        log = log_list.pop(i)
        log_list.append(log)
    for i in range(N):
        dif.append(abs(final_list[i] - final_list[i - 1]))
    return max(dif)
for _ in range(T):
    print(hopping())
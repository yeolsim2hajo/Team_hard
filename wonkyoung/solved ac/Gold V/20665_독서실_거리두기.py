#221210
# N, T, P = map(int, input().split())
# # 사용자 입실, 퇴실 시간
# user_check_info = sorted([input().split() for _ in range(T)], key=lambda x: (x[0], x[1]))
# # 각 자리가 차있을 때, 퇴실 시간
# seat_info = [''] * (N+1)
# # 차 있는 자리
# occupied = set()
# # 관리자가 이용할 수 있는 시간
# total_time = 720
# # 자리가 차는 순서
# seat_order = [1]
#
# # 자리가 차는 순서 찾기
# def find_seat_order():
#     if N > 1:
#         from heapq import heappush, heappop
#         visited = {1}
#         heap = []
#         heappush(heap, (-N+1, 1, N))
#         while heap:
#             minus_gap, start, end = heappop(heap)
#             mid = (start + end) // 2
#             for i in (start, end, mid):
#                 if i not in visited:
#                     visited.add(i)
#                     seat_order.append(i)
#             if start != mid != end:
#                 heappush(heap, (start - mid, start, mid))
#                 heappush(heap, (mid - end, mid, end))
#
# def choose_seat():
#     # 시간이 다 된 좌석 있는지 확인
#     pre_occupied = set(occupied)
#     for seat_num in pre_occupied:
#         if seat_info[seat_num] and seat_info[seat_num] <= check_in:
#             seat_info[seat_num] = ''
#             occupied.remove(seat_num)
#     # 배치할 좌석 찾기
#     for j in seat_order:
#         if j not in occupied:
#             return j
#
# find_seat_order()
#
# for i in range(T):
#     check_in, check_out = user_check_info[i]
#     # 좌석에 배치
#     user_seat = choose_seat()
#     seat_info[user_seat] = check_out
#     occupied.add(user_seat)
#     # 시간 계산
#     if user_seat == P:
#         start_hour, start_min = map(int, [check_in[:2], check_in[2:]])
#         end_hour, end_min = map(int, [check_out[:2], check_out[2:]])
#         total_time -= (end_hour - start_hour) * 60 + (end_min - start_min)
# print(total_time)


#221211
N, T, P = map(int, input().split())
# 사용자 입실, 퇴실 시간
user_check_info = sorted([input().split() for _ in range(T)], key=lambda x: (x[0], x[1]))
# 각 자리가 차있을 때, 퇴실 시간
seat_info = [''] * (N+1)
# 차 있는 자리
occupied = set()
# 관리자가 이용할 수 있는 시간
total_time = 720
# 자리가 차는 순서
seat_order = [1]

# 자리가 차는 순서 찾기
def find_seat_order():
    if N > 1:
        from heapq import heappush, heappop
        visited = {1}
        heap = []
        heappush(heap, (-N+1, 1, N))
        while heap:
            minus_gap, start, end = heappop(heap)
            mid = (start + end) // 2
            for i in (start, end, mid):
                if i not in visited:
                    visited.add(i)
                    seat_order.append(i)
            if start != mid != end:
                heappush(heap, (start - mid, start, mid))
                heappush(heap, (mid - end, mid, end))

def choose_seat():
    from heapq import heappush, heappop
    # 시간이 다 된 좌석 있는지 확인
    pre_occupied = set(occupied)
    for seat_num in pre_occupied:
        if seat_info[seat_num] and seat_info[seat_num] <= check_in:
            seat_info[seat_num] = ''
            occupied.remove(seat_num)
    # 배치할 좌석 찾기
    heap = []
    for j in seat_order:
        if not occupied:
            return j
        elif j not in occupied:
            total, length = 0, len(occupied)
            # length = len(occupied)
            for k in occupied:
                total += j-k
            heappush(heap, (-abs(total/length), j))
    print(heap)
    return heappop(heap)[1]

find_seat_order()
# print(seat_order)

for i in range(T):
    check_in, check_out = user_check_info[i]
    # 좌석에 배치
    user_seat = choose_seat()
    print(user_seat)
    seat_info[user_seat] = check_out
    occupied.add(user_seat)
    # 시간 계산
    if user_seat == P:
        start_hour, start_min = map(int, [check_in[:2], check_in[2:]])
        end_hour, end_min = map(int, [check_out[:2], check_out[2:]])
        total_time -= (end_hour - start_hour) * 60 + (end_min - start_min)
print(total_time)
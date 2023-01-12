#230106
# 시간 초과
# N = int(input())
# numbers = list(map(int, input().split()))
# cnt = 1
# path = []
# def find_cnt(limit, level=0, start=0):
#     global cnt
#     if level == limit:
#         cnt = limit
#         return
#     for j in range(start, N):
#         number = numbers[j]
#         if not path or path[-1] < number:
#             path.append(number)
#             find_cnt(limit, level+1, j+1)
#             path.pop()
# for i in range(N, 1, -1):
#     find_cnt(i)
#     if cnt != 1:
#         break
# print(cnt)


# 다른 방법
N = int(input())
numbers = list(map(int, input().split()))
cnt = 1
def find_cnt(start):
    answer = 1
    # last = numbers[start]
    path = [numbers[start]]
    for j in range(start+1, N):
        number = numbers[j]
        if path[-1] < number:
        # if last < number:
        #     last = number
            path.append(number)
            answer += 1
    print(path, answer)
    return answer
for i in range(N-1):
    if N-i > cnt:
        new_cnt = find_cnt(i)
        if cnt < new_cnt:
            cnt = new_cnt
print(cnt)
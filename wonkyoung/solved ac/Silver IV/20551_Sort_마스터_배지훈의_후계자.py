#230110
# sort
# import sys
# new_input = sys.stdin.readline
# N, M = map(int, new_input().split())
# arr = [int(new_input()) for _ in range(N)]
# arr.sort()
# position = {}
# for i in range(N):
#     position.setdefault(arr[i], i)
# for _ in range(M):
#     number = int(new_input())
#     if position.get(number, -1) != -1:
#         answer = position[number]
#     else:
#         answer = -1
#     print(answer)

# sorted
# import sys
# new_input = sys.stdin.readline
# N, M = map(int, new_input().split())
# arr = sorted([int(new_input()) for _ in range(N)])
# position = {}
# for i in range(N):
#     position.setdefault(arr[i], i)
# for _ in range(M):
#     number = int(new_input())
#     if position.get(number, -1) != -1:
#         answer = position[number]
#     else:
#         answer = -1
#     print(answer)

# try-except
# import sys
# new_input = sys.stdin.readline
# N, M = map(int, new_input().split())
# arr = [int(new_input()) for _ in range(N)]
# arr.sort()
# position = {}
# for i in range(N):
#     position.setdefault(arr[i], i)
# for _ in range(M):
#     number = int(new_input())
#     try:
#         answer = position[number]
#     except:
#         answer = -1
#     print(answer)


# 함수형
def main():
    import sys
    new_input = sys.stdin.readline
    N, M = map(int, new_input().split())
    arr = [int(new_input()) for _ in range(N)]
    position = {}
    def fill_position():
        arr.sort()
        for i in range(N):
            position.setdefault(arr[i], i)
    def find_answer():
        number = int(new_input())
        if position.get(number, -1) != -1:
            return position[number]
        return -1
    fill_position()
    for _ in range(M):
        print(find_answer())
main()

#221102
# N = int(input())
# students = [0]*N
# match = [[0]*5 for _ in range(N)]
# info = []
# for i in range(N):
#     student = list(map(int, input().split()))
#     info.append(student)
#     for j in range(5):
#         match[j][i] += 1
#
# info = list(zip(*info))
# for i in range(N):
#     for j in range(5):
#         students[i] += info[i].count(info[i][j]) - 1
#         print(students[i], 's')
#         print(info[i][j], 'i')
# max_val = 0
# print(students)
# for i in range(N):
#     if max_val < students[i]:
#         candidate = i
#         max_val = students[i]
# print(candidate+1)

# 3차원 리스트
# import sys, pprint
#
# # 학년, 반, 학생들
# match = [[[] for _ in range(10)] for _ in range(5)]
# new_input = sys.stdin.readline
# N = int(new_input())
# # 번호, 학년, 반
# info = [[0] * (N)]
# for i in range(1, N+1):
#     student_info = list(map(int, input().split()))
#     info.append(student_info)
#     for j in range(5):
#         match[j][student_info[j]].append(i)
#
# cnt = [0]*(N+1)
# for i in range(1, N+1):
#     for j in range(5):
#         cnt[i] += len(match[j][info[i][j]]) - 1
#
# max_val = 0
# for i in range(1, N+1):
#     if cnt[i] > max_val:
#         max_val = cnt[i]
#         answer = i
# print(answer)


# 다시
# import sys
#
# # 학년, 반, 학생들
# match = [[set() for _ in range(10)] for _ in range(5)]
# new_input = sys.stdin.readline
# N = int(new_input())
# # 번호, 학년, 반
# info = [[0] * N]
# for i in range(1, N+1):
#     student_info = list(map(int, input().split()))
#     info.append(student_info)
#     for j in range(5):
#         match[j][student_info[j]].add(i)
#
# students = [set() for _ in range(N+1)]
# cnt = [0] * (N+1)
# for i in range(1, N+1):
#     for j in range(5):
#         students[i].update(match[j][info[i][j]])
#     cnt[i] = len(students[i])
#
# max_val = -1
# for i in range(1, N+1):
#     if cnt[i] > max_val:
#         max_val = cnt[i]
#         answer = i
# print(answer)


# cnt 숫자 변수로
# import sys
#
# # 학년, 반, 학생들
# match = [[set() for _ in range(10)] for _ in range(5)]
# new_input = sys.stdin.readline
# N = int(new_input())
# # 번호, 학년, 반
# info = [[0] * N]
# for i in range(1, N+1):
#     student_info = list(map(int, input().split()))
#     info.append(student_info)
#     for j in range(5):
#         match[j][student_info[j]].add(i)
#
# students = [set() for _ in range(N+1)]
# for i in range(1, N+1):
#     for j in range(5):
#         students[i].update(match[j][info[i][j]])
#
# max_val = -1
# for i in range(1, N+1):
#     cnt = len(students[i])
#     if cnt > max_val:
#         max_val = cnt
#         answer = i
# print(answer)


# 최적화 시도
# import sys
#
# # 학년, 반, 학생들
# match = [[set() for _ in range(10)] for _ in range(5)]
# new_input = sys.stdin.readline
# N = int(new_input())
# # 번호, 학년, 반
# for i in range(1, N+1):
#     student_info = list(map(int, input().split()))
#     for j in range(5):
#         match[j][student_info[j]].add(i)
#
# students = [set() for _ in range(N+1)]
# for i in range(5):
#     for j in range(1, 10):
#         student_set = match[i][j]
#         for idx in student_set:
#             students[idx].update(student_set)
#
# max_val = -1
# for i in range(1, N+1):
#     cnt = len(students[i])
#     if cnt > max_val:
#         max_val = cnt
#         answer = i
# print(answer)


# 함수형
# def find_leader():
#     import sys
#     # 학년, 반, 학생들
#     match = [[set() for _ in range(10)] for _ in range(5)]
#     new_input = sys.stdin.readline
#     N = int(new_input())
#     # 번호, 학년, 반
#     for i in range(1, N+1):
#         student_info = list(map(int, input().split()))
#         for j in range(5):
#             match[j][student_info[j]].add(i)
#
#     students = [set() for _ in range(N+1)]
#     for i in range(5):
#         for j in range(1, 10):
#             student_set = match[i][j]
#             for idx in student_set:
#                 students[idx].update(student_set)
#
#     max_val = -1
#     for i in range(1, N+1):
#         cnt = len(students[i])
#         if cnt > max_val:
#             max_val = cnt
#             answer = i
#     return answer
# print(find_leader())


# new_input 사용
def find_leader():
    import sys

    match = [[set() for _ in range(10)] for _ in range(5)]
    new_input = sys.stdin.readline
    N = int(new_input())

    for i in range(1, N + 1):
        student_info = list(map(int, new_input().split()))
        for j in range(5):
            match[j][student_info[j]].add(i)

    students = [set() for _ in range(N + 1)]
    for i in range(5):
        for j in range(1, 10):
            student_set = match[i][j]
            for idx in student_set:
                students[idx].update(student_set)

    max_val = -1
    for i in range(1, N + 1):
        cnt = len(students[i])
        if cnt > max_val:
            max_val = cnt
            answer = i
    return answer

print(find_leader())
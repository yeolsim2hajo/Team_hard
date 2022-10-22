#221022
# from heapq import heappop, heappush
# N, HP = map(int, input().split())
# skills = []
# for _ in range(N):
#     C, D = map(int, input().split())
#     # 현재 시각, 남은 체력, 공격력, 대기 시간
#     heappush(skills, (0, HP, 0, -D/C, -D, C))
# min_time = HP
#
# while True:
#     now, bar, power, wait = heappop(skills)
#     if bar < 0:
#         min_time = min(min_time, now)


# dfs 사용
# 시간 초과 => 성공
# N, HP = map(int, input().split())
# skills = [list(map(int, input().split())) + [0] for _ in range(N)]
# min_time = HP
#
# def dfs(now, left, changed):
#     global min_time
#     if now >= min_time:
#         return
#     if left <= 0:
#         min_time = now
#         return
#
#     new_changed = []
#     for i in range(N):
#         new_changed.append(changed[i][:])
#         if new_changed[i][2]:
#             new_changed[i][2] -= 1
#
#     for i in range(N):
#         if new_changed[i][2] == 0:
#             new_changed[i][2] = new_changed[i][0]
#             dfs(now+1, left-skills[i][1], new_changed)
#             new_changed[i][2] = 0
#     dfs(now + 1, left, new_changed)
#
# for j in range(N):
#     new_skills = [skills[k][:] for k in range(N)]
#     new_skills[j][2] = new_skills[j][0]
#     dfs(1, HP-new_skills[j][1], new_skills)
#
# print(min_time)


# 최적화 시도
# N, HP = map(int, input().split())
# skills = [list(map(int, input().split())) + [0] for _ in range(N)]
# min_time = HP
# skills.sort(key=lambda skill:skill[1], reverse=True)
#
# def dfs(now, left, changed):
#     global min_time
#     if now >= min_time:
#         return
#     if left <= 0:
#         min_time = now
#         return
#
#     new_changed = []
#     for i in range(N):
#         new_changed.append(changed[i][:])
#         if new_changed[i][2]:
#             new_changed[i][2] -= 1
#
#     for i in range(N):
#         if new_changed[i][2] == 0:
#             new_changed[i][2] = new_changed[i][0]
#             dfs(now+1, left-skills[i][1], new_changed)
#             new_changed[i][2] = 0
#     dfs(now + 1, left, new_changed)
#
# for j in range(N):
#     new_skills = [skills[k][:] for k in range(N)]
#     new_skills[j][2] = new_skills[j][0]
#     dfs(1, HP-new_skills[j][1], new_skills)
#
# print(min_time)


# 최적화 시도2
# N, HP = map(int, input().split())
# skills = [list(map(int, input().split())) + [0] for _ in range(N)]
# min_time = HP
# skills.sort(key=lambda skill:(-skill[1], skill[0]))
#
# def dfs(now, left, changed):
#     global min_time
#     if now >= min_time:
#         return
#     if left <= 0:
#         min_time = now
#         return
#
#     new_changed = []
#     for i in range(N):
#         new_changed.append(changed[i][:])
#         if new_changed[i][2]:
#             new_changed[i][2] -= 1
#
#     for i in range(N):
#         if new_changed[i][2] == 0:
#             new_changed[i][2] = new_changed[i][0]
#             dfs(now+1, left-skills[i][1], new_changed)
#             new_changed[i][2] = 0
#     dfs(now + 1, left, new_changed)
#
# for j in range(N):
#     new_skills = [skills[k][:] for k in range(N)]
#     new_skills[j][2] = new_skills[j][0]
#     dfs(1, HP-new_skills[j][1], new_skills)
#
# print(min_time)
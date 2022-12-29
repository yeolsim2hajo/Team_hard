#221229
# name = input()
# N = int(input())
# keys = 'LOVE'
# love = [0] * 4
# for alp in name:
#     for i in range(4):
#         if keys[i] == alp:
#             love[i] += 1
#             break
# propability, final_team = 0, 'Z' * 20
# for _ in range(N):
#     love_temp = love[:]
#     team = input()
#     for alp in team:
#         for i in range(4):
#             if keys[i] == alp:
#                 love_temp[i] += 1
#                 break
#     answer = 1
#     for i in range(4):
#         for j in range(i+1, 4):
#             answer *= love_temp[i] + love_temp[j]
#     answer %= 100
#     if propability < answer:
#         propability = answer
#         final_team = team
#     elif propability == answer and final_team > team:
#         final_team = team
# print(final_team)


# 정렬 - 시간 더 걸림, 메모리 줄어듦
# name = input()
# N = int(input())
# keys = 'LOVE'
# love = [0] * 4
# for alp in name:
#     for i in range(4):
#         if keys[i] == alp:
#             love[i] += 1
#             break
# teams = sorted([input() for _ in range(N)])
# propability, final_team = 0, teams[0]
# for index in range(N):
#     love_temp = love[:]
#     team = teams[index]
#     for alp in team:
#         for i in range(4):
#             if keys[i] == alp:
#                 love_temp[i] += 1
#                 break
#     answer = 1
#     for i in range(4):
#         for j in range(i+1, 4):
#             answer *= love_temp[i] + love_temp[j]
#     answer %= 100
#     if propability < answer:
#         propability = answer
#         final_team = team
# print(final_team)


# 함수
def change_value(target_str, target_list):
    keys = 'LOVE'
    for alp in target_str:
        for i in range(4):
            if keys[i] == alp:
                target_list[i] += 1
                break

def change_answer():
    global propability, final_team
    answer = 1
    for i in range(4):
        for j in range(i+1, 4):
            answer *= love_temp[i] + love_temp[j]
    answer %= 100
    if propability < answer:
        propability = answer
        final_team = team
    elif propability == answer and final_team > team:
        final_team = team

name = input()
N = int(input())
love = [0] * 4
change_value(name, love)
propability, final_team = 0, 'Z' * 20
for _ in range(N):
    love_temp = love[:]
    team = input()
    change_value(team, love_temp)
    change_answer()
print(final_team)

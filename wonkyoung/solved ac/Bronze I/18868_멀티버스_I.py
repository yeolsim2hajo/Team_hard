#230206
# enumerate
# universe, planet = map(int, input().split())
# universe_info = [sorted(enumerate(map(int, input().split())), key=lambda x : x[1]) for _ in range(universe)]
# universe = len(universe_info)
# cnt = 0
#
# for i in range(universe-1):
#     one = universe_info[i]
#     for j in range(i+1, universe):
#         two = universe_info[j]
#         for k in range(planet-1):
#             if bool(one[k][1] == one[k+1][1]) is not bool(two[k][1] == two[k+1][1]):
#                 break
#             elif one[k][0] != two[k][0]:
#                 break
#         else:
#             cnt += 1
# print(cnt)


# 함수화
def find_parallel():
    universe, planet = map(int, input().split())
    universe_info = [sorted(enumerate(map(int, input().split())), key=lambda x : x[1]) for _ in range(universe)]
    universe = len(universe_info)
    cnt = 0

    for i in range(universe-1):
        one = universe_info[i]
        for j in range(i+1, universe):
            two = universe_info[j]
            for k in range(planet-1):
                if bool(one[k][1] == one[k+1][1]) is not bool(two[k][1] == two[k+1][1]):
                    break
                elif one[k][0] != two[k][0]:
                    break
            else:
                cnt += 1
    return cnt

print(find_parallel())


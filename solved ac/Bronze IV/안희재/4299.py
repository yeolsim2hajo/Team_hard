a, b = map(int,input().split())

if a-b < 0 or (a-b) % 2 != 0 or (a+b) % 2 != 0:
    print(-1)
else:
    team1 = abs((a+b)//2)
    team2 = abs((a-b)//2)

    print(max(team1,team2), min(team1,team2))


# 처음 코드 - 마지막에 max, min이 더 간단할 듯
# team1 = abs((a+b)//2)
# team2 = abs((a-b)//2)

# if team1 > team2:
#     print(team1, team2)
# else:
#     print(team2, team1)
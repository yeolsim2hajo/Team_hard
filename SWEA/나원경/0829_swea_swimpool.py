T = int(input())
for tc in range(1, 1 + T):
    day, month, quarter, year = map(int, input().split())
    plan = list(map(int, input().split()))
    cost = [0] * 12
    for i in range(12):
        month_cnt = plan[i]
        cost[i] = min(month_cnt * day, month)
    total_cost = sum(cost)

    def dfs(start=0, new_cost=total_cost):
        global total_cost
        if start >= 12:
            total_cost = min(total_cost, new_cost)
            return
        for i in range(start, 10):
            quarter_cost = sum(cost[i:i + 3])
            if quarter_cost > quarter:
                dfs(i + 3, new_cost - quarter_cost + quarter)
        total_cost = min(total_cost, new_cost)

    dfs()

    total_cost = min(total_cost, year)
    print(f'#{tc} {total_cost}')
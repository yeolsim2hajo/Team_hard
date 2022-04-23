# 최종 / 원경수정(deepcopy대신에, insert쓰니까, 실행시간 1/10로 줄어들긴 했음! 굿굿)
# 근데, 여전히.. 음;;; 별로인듯 이 방식이 최종적으로.
def solution(tickets):
    all_number = len(tickets)+1
    path = []
    answer = []

    def dfs(start):
        nonlocal tickets, path
        tmp = [x[0] for x in tickets]
        if not start in tmp:
            path.append(start)
            if len(path) < all_number:
                return
            else:
                answer.append(path[:])
                return

        tmp2 = path[:]
        for i in range(len(tickets)):
            if tickets[i][0] != start: continue
            path.append(start)
            next = tickets[i][:]
            tickets.pop(i)
            dfs(next[1])
            path = tmp2[:]
            tickets.insert(i,next)

    dfs('ICN')
    answer.sort()
    return answer[0]
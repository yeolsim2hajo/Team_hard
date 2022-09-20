import copy

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

        tmp2 = copy.deepcopy(tickets)
        tmp3 = path[:]
        for i in range(len(tickets)):
            if tickets[i][0] != start: continue
            path.append(start)
            next = tickets[i][1]
            tickets.pop(i)
            dfs(next)
            path = tmp3[:]
            tickets = copy.deepcopy(tmp2)

    dfs('ICN')
    answer.sort() 
    return answer[0]
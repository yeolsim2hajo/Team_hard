# 최종 코드------------------------
tickets = [["ICN", "AOO"], ["AOO", "BOO"], ["BOO", "COO"], ["COO", "DOO"], ["DOO", "EOO"], ["EOO", "DOO"], ["DOO", "COO"], ["COO", "BOO"], ["BOO", "AOO"]]
path = [] # return값

# 출발지가 departure인 항공권 중에서 도착지의 알파벳이 가장 빠른 것 리턴하는 함수
def fast(departure):
    tmp = []
    for i in range(len(tickets)):
        if tickets[i][0] == departure:
            tmp.append((i,tickets[i][1])) # 인덱스와, 도착도시정보를 담음 (인덱스는 나중에 pop할거기때문에 필요

    tmp.sort(key=lambda x: ord(x[1][0]))
    
    

    return tmp[0][1], tmp[0][0] # 튜플 반환(다음 출발도시, 인덱스) 및 그대로 dfs에 인자로 넣을 것

def dfs(start, ridx): # ridx는 지울 인덱스. 정확히는 이전꺼.
    if ridx >= 0:
        tickets.pop(ridx)

    if len(tickets) == 0:
        path.append(start)
        return

    path.append(start)
    a, b = fast(start)
    dfs(a, b)

dfs("ICN",-1) # 처음엔 안 지움
print(path)

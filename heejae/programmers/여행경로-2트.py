# dfs인듯 
# 주어진 항공권은 모두 사용해야 합니다.
# 모든 도시를 방문할 수 없는 경우는 주어지지 않습니다.
# -> level이 항공권개수에 도달하면 path 출력하면 될듯?

# 1트: 테케1,2 -> 런타임 에러
    # 이유가 무엇인가? -> 알파벳순이긴한데, 만약 첫 알파벳이 같으면?? ㅠㅠ? ㄴㄴ;;;
    # 아;; 선택했는데 갈 수 없으면? 즉, 맨-마지막 종착지인 경우: 그 도시의 도착지 없잖아 ㅠㅠ
    # 이걸 도대체 어떻게 생각하지..? 코테는 다 이런가 와;; 미치겠다 진짴
    # 일단, 완주할 수 있는가에 대한 코드가 빈약함. 단순히, 다음 출발지로 가능? 노놉;;너무 1차원적임
# ---------------------------------------------------------------

tickets =[["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]
path = [] # return값

# 출발지가 departure인 항공권 중에서 도착지의 알파벳이 가장 빠른 것 리턴하는 함수
def fast(departure):
    tmp = []
    for i in range(len(tickets)):
        if tickets[i][0] == departure:
            tmp.append((i,tickets[i][1])) # 인덱스와, 도착도시정보를 담음 (인덱스는 나중에 pop할거기때문에 필요


    tmp.sort(key=lambda x: ord(x[1][0]))

    tmp2 = [x[0] for x in tickets] # 출발지만 딴 임시 배열
    if len(tickets) != 1 and not tmp[0][1] in tmp2: # 다음 출발예정지인 도시가 없다면, 최종 종착역이라는 뜻
        tmp.pop(0) # 따라서, 다음 알파벳순으로 넘겨

    return tmp[0][1], tmp[0][0] # 튜플 반환 및 그대로 dfs에 인자로 넣을 것

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

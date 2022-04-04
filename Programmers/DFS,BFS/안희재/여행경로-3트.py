# dfs(start)로 짜긴 하되, "가능한" 경우를 다 탐색
    # 언제까지? start로 갈 수 있는데가 없을때 까지
    # 단, path의 길이가 모든 항공권 사용한 경우보다 적으면? answer리스트에 추가 x
        # 다 사용한 경우 경로의 길이: len(tickets)+1
    # 결과적으로 모든 항공권을 사용한 path정보만 answer에 담음
    # 그리고, answer의 각 요소를 비교해서, 다른게 발견되면?
        # 알파벳순인 경우겠지 -> 알파벳 순을 더 빠른걸 choose!
        # 탈락은 pop!

# 아... 이것도 tc1 통과 안되네;;;
# 사실 좋은 코드가 아니라는 것은 아는데; 도대체 왜 1번케이스만 시간과 메모리가 엄청 걸리는가?
    # tmp3 = path[:]로 tc1도 통과는 됨
    # 그러나, 여전히 시간은 엄청 걸림 도대체 왜 그런것인가?
        # deepcopy? -> tc1이 n이 엄청 큰 경우인가? 그래서 deepcopy도 엄청 많이해서?
        # 그렇다면 어떻게 복구를 해야하는가? 이 방법은 아예 틀린 것인가?
        # 애초에, dfs안에서 알파벳순을 출력하는게 정석이긴 함. 나는 엄밀히 말하면 운이 좋았고, 야매식.
        # 그럼에도 불구하고 이유는 알고 싶음.
# ------------------------------------------------------
import copy

tickets = [["ICN", "JFK"], ["HND", "ICN"], ["JFK", "HND"]]
all_number = len(tickets)+1 # 모든 항공권을 사용한 경우 출력되는 도시들의 개수
path = [] # 가능한 최종 경로
answer = [] # path들의 모음(여기서 알파벳순인 것을 뽑을 예정)

def dfs(start):
    global tickets, path
    tmp = [x[0] for x in tickets] # tickets의 0번인덱스(즉, 출발지)들만 모은 배열
    if not start in tmp: # 더 이상 갈 수 없으면 return
        path.append(start) # start지만 갈 수 없음 => "종착점"이므로 path의 마지막에 추가
        if len(path) < all_number: # 그런데, 모든 항공권을 다 사용못했다면 컷!
            return
        else:
            answer.append(path[:]) # 항공권 다 사용했다면, 최종 answer목록에 path경로들을 추가
            return

    tmp2 = copy.deepcopy(tickets) # 원상복구
    tmp3 = path[:] # 복사문제 방지
    for i in range(len(tickets)):
        if tickets[i][0] != start: continue # 출발지가 아니면 pass
        path.append(start) # (start= tickets[i][1]인 경우 -> 현재의 출발지를 path에 추가하고)
        next = tickets[i][1] # 현재의 도착지를 -> 다음 dfs의 출발지로 저장
        tickets.pop(i) # 사용한 항공권은 빼주기
        dfs(next) 
        # path = tmp3 # dfs 빠져나올 때는 path와 tickets 원상복구
        path = tmp3[:] # [:]써야 겨우 작동함;; 여기서도 얕은복사해야하나봐;;
        tickets = copy.deepcopy(tmp2) 

dfs('ICN')
answer.sort() # 그냥 이렇게 하면 알파벳순으로 정렬됨 ㄷㄷ;
print(answer[0])

# -------------------------------------------
# while 1:
#     result = [] # 흠;; 
#     if len(result) == 1:
#         print(result[0])
    
#     start = 1 # 어차피 모든 시작점은 ICN이므로 1번인덱스부터 알파벳 검사
#     idx, Min = -1, 2e18
#     for i in range(len(answer)):
#         if answer[i][start][0]
#           ...        


# - 안끝나나?
# 누가 개강총회에 왔는지 알 수 없다
# 누가 개강총회 자리에 끝까지 남아있었는지 알 수 없다
# 어떤 사람이 개강총회 스트리밍을 단순히 틀어놓기만 했는지 알 수 없다 -> 확인사살까지 필요

import sys
input = sys.stdin.readline

start, end, stream = input().split()
start = int(start[:2] + start[3:])
end = int(end[:2] + end[3:])
stream = int(stream[:2] + stream[3:])

student = set() # 중복처리를 위해 set -> list는 시간초과 되는 경우도 있었음
answer = 0

while True: # 두번째 줄 부터 입력되는 학회원의 명단 수를 알 수 없으므로, while 무한반복문을 만들어주고, 안에서 break문을 따로 만들어 줌
    try: # try except문: 더 이상 try문의 내용이 발생하지 않으면, except => break로 while문 종료
        time, name = input().split() # 학회원의 채팅시간과, 이름
        time = int(time[:2] + time[3:])
        if time <= start: # 일단, 개강총회 시작 이전에 입장했다면, 무조건 추가
            student.add(name)
        elif end <= time <= stream and name in student: # 개강총회 종료 ~ 스트리밍 종료사이에 채팅을 남겼으며, 입장 기록이 있다면(=student에 추가됨) 출석완료!
            student.remove(name) # 처리했다면, 이제 다시 목록에서 빼줘야 함
            answer += 1 # cnt해주기
    except:
        break

print(answer)
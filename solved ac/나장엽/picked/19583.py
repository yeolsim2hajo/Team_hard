# 입장 여부 확인 -> 시작 시간 이전에 대화 기록, 시작하자마자 남긴 대화 기록 -> ok,
# 퇴장 여부 확인 -> 개강 총회가 끝나자마자 대화기록, 개강총회 스트리밍이 끝나자마자 대화기록 -> ok

# 00:00부터는 개강총회를 시작하기 전의 대기 시간, 개강총회 스트리밍이 끝난 이후로 남겨져 있는 채팅기록은 
# 다른 스트리밍 영사으이 대화기록으로 간주
# 입장부터 퇴장까지 모두 확인된 학회원의 수를 구해라.
import sys
input = sys.stdin.readline
s, e, q = map(str, input().split())

# 해시 사용
data = dict()
result = dict()

while True:
    try:
        time, nick = input().split()
        if time <= s: # 개총 시작 시간보다 일찍 들어온 사람 확인 후 data에 할당
            data[nick] = time 
        elif e <= time <= q: # 개총 종료시간 ~ 스트리밍 종료시간 사이에 들어온 사람
            if nick in data: # 개총 시작보다 일찍 들어온 사람이면 result에 할당
                result[nick] = 1
    except:
      break

print(len(result))
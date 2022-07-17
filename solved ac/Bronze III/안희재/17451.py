# answer -> speed가 더 나은듯
# point: 맨 뒤에서부터 탐색해서 모든 행성을 순서대로 탐색했을 때 통과할 수 있는 최소 스피드 찾기

# 300 400 500 400 300
# 거꾸로
# 300 400 500 400 300

# 300-400-500-800-900


n = int(input())
planets = list(map(int,input().split()))
answer = planets[-1] 

for i in range(n-2, -1, -1): # 뒤에서부터 2번째부터 역순으로 탐색
    if planets[i] > answer: # 만약, 행성속도가 현재 속도보다 크다면, 갱신
        answer = planets[i]
    else: # "행성속도가 현재 속도 이하" + "정수배x" => 최소배수로 갱신
        if answer%planets[i]: # 정수배가 x
            answer = (answer//planets[i] + 1) *planets[i]
print(answer) 
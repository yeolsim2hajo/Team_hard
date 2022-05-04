
N = int(input())
result = [list(input()) for _ in range(N)]

for i in range(len(result)):
    score = 0 # 누적합
    num = 1 # 점수 1 초기화 
    for k in range(len(result[i])):
        if result[i][k] == 'O':
            score += num
            num += 1 # 연속으로 정답이면 +1 

        elif result[i][k] == 'X':
            num = 1 # 틀리면 다시 1로 초기화  

    print(score) # result의 케이스마다 점수 출력.

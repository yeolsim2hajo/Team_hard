# a1 = [1]
# a2 = [1,1]
# a3 = [1,2,1]
# a4 = [1,3,3,1] # a3스택의 0, 0+1, 1+2, 2
# a5 = [1,4,6,4,1] # a4스택의 0, 0+1, 1+2, 2+3, 3
# 양 옆에 1(a1,2제외)
# a3은 가운데가 1개 / a4는 가운데 2개 / a5는 가운데 3개 ... aN은 가운데 N-2개
# stack에 이전꺼 쌓아두고, 다음 줄은 스택꺼 더하는 식으로
# 넘어가기 전에 stack 갱신하고
# 피보나치랑 비슷한데, 재귀 + 스택 이용해야하나? ㅇㅇ
# ---------------------------------------------------------------

# 파스칼 삼각형 : 다음 줄은 피보나치처럼 이전 줄에 의해 생성되기에,
# 재귀 + 스택 개념 이용해서 해결

T = int(input())
for tc in range(1,T+1):
    N = int(input())

    result = [[1], [1,1]]
    stack = [1,1] # 이것도 밖에다 둬야함. 안 그러면, 매 번마다 [1,1]로 초기화됨
    # (비록, stack = arr을 준다고 해도.)

    def pascal(level): # num >=3 인 경우에만 pascal함수 사용
        global result, stack
        if level == N+1: # 처음 시작이 pascal(3)이기 때문에, N+1
            return
        
        arr = [1] * level # 모든 숫자를 일단, 1로 바꿔놓고 가운데 숫자를 아래 코드를 통해 채운다
        for i in range(1,level-1): # level=3 -> i= 1 // level=4 -> i = 1,2
            arr[i] = stack[i-1] + stack[i] # arr[1] = stack[1] +stack[2]
        
        result.append(arr)
        stack = arr # stack을 변화된 arr로 초기화
        pascal(level+1)
        
    if N == 1:
        print(f'#{tc}')
        print(1)
    elif N == 2:
        print(f'#{tc}')
        for i in range(2):
            print(*result[i])
    else:
        pascal(3)
        # 이거 재귀 처음 연습했을때처럼, 재귀함수 바로 아래쪽에 쓰면 에러뜸
        # N = 1인 경우, 무한반복이기 때문.
        print(f'#{tc}')
        for i in range(N):
            print(*result[i])

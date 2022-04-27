N = int(input())

result = [[1], [1,1]]
stack = [1,1] # 이것도 밖에다 둬야함. 안 그러면, 매 번마다 [1,1]로 초기화됨
# (비록, stack = arr을 준다고 해도.)

def pascal(level): # num >=3 인 경우에만 pascal함수 사용
    global result, stack
    if level == N+1: # 처음 시작이 pascal(3)이기 때문에, N+1
        print(result)
        return
    
    arr = [1] * level # 모든 숫자를 일단, 1로 바꿔놓고 가운데 숫자를 아래 코드를 통해 채운다
    for i in range(1,level-1): # level=3 -> i= 1 // level=4 -> i = 1,2
        arr[i] = stack[i-1] + stack[i] # arr[1] = stack[1] +stack[2]
    
    result.append(arr)
    stack = arr
    pascal(level+1)
    

if N == 1:
    print(1)
elif N == 2:
    for i in range(2):
        print(*result[i])
else:
    pascal(3) # 이거 재귀 처음 연습했을때처럼, 재귀함수 바로 아래쪽에 쓰면 에러뜸
            # N = 1인 경우, 무한반복이기 때문.
    for i in range(N):
        print(*result[i])
# 예1 : ( {} () {} ) -> true
# 예2 : ( { ) } -> false
# 예3 : ( {} {} ( () ) -> false
T = int(input())

for tc in range(1,T+1):
    word = input()

    def check():
        stack = []
        result = 1
        for i in range(len(word)):
            if word[i] == '(' or word[i] == '{': # 여는 괄호의 경우 바로 추가
                stack.append(word[i]) 
            elif word[i] == ')' or word[i] == '}': # 닫는 괄호나오면, 특정 조건하에서만 빼줌
                if len(stack) == 0:
                    result = 0 # 스택이 비어있을 때, 닫는 괄호 시작이면 바로 컷
                    return result
                elif word[i] == ')' and stack[-1] == '{': # 짝이 안 맞게 이어진 경우 바로 컷(예2)
                    result = 0
                    return result
                elif word[i] == '}' and stack[-1] == '(':
                    result = 0
                    return result
                else: # 직전과 짝이 맞다면 계속!
                    stack = stack[0:len(stack)-1] # 마지막 pop

        if len(stack) != 0: # 반복문 다 돌리고나서, stack이 남아있으면 짝이 안맞는 것
            result = 0
            return result
        return result # 위 반복문, 조건문에서 return이 걸리지 않는다면, result = 1가 리턴


    print(f'#{tc}', check())


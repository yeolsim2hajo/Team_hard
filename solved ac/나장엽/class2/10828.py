# 정수를 저장하는 스택을 구현한 다음, 명령어를 처리하는 프로그램 작성
import sys

def cmd(data):
    command = data[0]
    
    # number를 스택에 넣기
    # push 일 경우에만 data[1]이 존재
    if command == 'push':
        number = data[1]
        stack.append(number)

    # 스택의 가장 위 정수를 빼고, 출력.
    # 정수가 없는 경우 -1 출력
    if command == 'pop':
        if len(stack) != 0:
            print(stack.pop())
        else:
            print(-1)

    # 스택에 들어있는 정수의 개수를 출력 -> len 함수
    elif command == 'size':
        print(len(stack))

    # 스택이 비어있으면 1 출력, 아니면 0 출력
    elif command == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)

    # 스택의 가장 위 정수를 출력
    # 없으면 -1 출력
    elif command == 'top':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])


N = int(input()) # command의 수
stack = [] # 스택

for i in range(N):
    data = sys.stdin.readline().split() # list 형으로 입력됨
    cmd(data)
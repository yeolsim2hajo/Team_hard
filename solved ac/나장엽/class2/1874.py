# stack : last in first out
# python에서는 list와 비슷함


# 주어진 수열 4, 3, 6, 8, 7, 5, 2, 1
# stack에 push 하는 순서는 오름차순. 
# 1, 2, 3, 4, 5, 6, 7.....
# stack을 이용하여 주어진 수열을 만들 수 있는지 판단.

from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
stack, answer, find = deque(), [], True # 스택, 결과값, 불가능, 가능 판단


now = 1 # 오름차순 
for i in range(N):
    number = int(input()) # 입력 받으면서, 수행
    while now <= number: # 입력받은 값보다 작으면 계속 push
        stack.append(now) 
        now += 1  
        answer.append('+') # push -> +
    if stack[-1] == number : # 입력값과 같으면 Pop
        stack.pop()
        answer.append('-') # pop -> -
    
    else: # 불가능 시 !
        find = False

if not find:
    print('NO')
else:
    for i in answer:
        print(i)
        
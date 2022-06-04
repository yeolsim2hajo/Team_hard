# # 스택 자료구조

# N = int(input())
# for i in range(N): # N번만큼 반복
#     temp = input()
#     stack = []
#     for i in temp:
#         if i == '(' : 
#             stack.append(i)
#         elif i == ')':
#             if len(stack) != 0 and stack[-1] == '(': # stack이 비어 있지않고, 최상단 값이 '(' 이면 ')'을 만나면 VPS
#                 stack.pop() # 위의 조건을 만족하면 pop
#             else:
#                 stack.append(')')
#                 break
    
#     if len(stack) == 0: # 모든 문자가 VPS면 stack의 길이는 0
#         print('YES') # 따라서 YES
#     else:
#         print('NO') 

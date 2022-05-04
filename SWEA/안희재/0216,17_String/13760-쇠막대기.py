# 총 2가지 (, ) / 그런데, 엄밀히 따지면 3가지임
# ( -> bar +1
# ) -> 
    # () : answer에 bar개수 추가, 
    # )) : bar -1 

T = int(input())

for tc in range(1, T+1):
    
    str = input()
    bar = 0 # 막대 개수
    cnt = 0 # 조각 개수

    for i in range(len(str)):
        if str[i] == '(':
            bar += 1 # 여는 괄호의 경우, 새 막대 시작이므로 1개씩 추가
                    # 레이저 여는 괄호인 경우 고려 안해도 됨. else문에서 -1하고 시작하기에
        else: # ')'의 경우
            bar -= 1 # 레이저 여는 괄호도 더해주기 때문에
            if str[i-1] == '(': # () - 레이저 완성
                cnt += bar 
            else: # )) - 막대 끝   
                cnt += 1 # 짧은 막대가 끝났으며, 마지막 조각(이전에 쪼개진 것 중) 추가

    print(f'#{tc} {cnt}')

# 서준 코드 - 내 코드보다 더 직관적인 듯
# --------------------------------------
# def Stick(arr):
#     sum1=0
#     cnt=0
#     for i in range(len(arr)):
#         if arr[i]=='('and arr[i+1] != ')':
#             sum1+=1
#         elif arr[i]==')'and arr[i-1] !='(':
#             cnt+=1
#             sum1-=1
#         elif arr[i]=='(' and arr[i+1]==')':
#             cnt+=sum1
#     return cnt
# --------------------------------------
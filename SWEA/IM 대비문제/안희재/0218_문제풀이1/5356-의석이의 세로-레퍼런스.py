# import sys
# sys.stadin = open('input_05.txt', 'r')

T = int(input())
for tc in range(1,T+1):
    arr = [list(input()) for _ in range(5)]
    sols = []
    for j in range(15): # 각 줄에 주어지는 문자열 길이는 1~15니까.
        for i in range(5):
            if j < len(arr[i]):
                sols.append(arr[i][j])
    print(f'#{tc}', ''.join(sols))

# Wow.........................

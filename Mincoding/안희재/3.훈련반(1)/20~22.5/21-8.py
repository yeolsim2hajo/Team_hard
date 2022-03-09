n = int(input())
arr = [input() for _ in range(n)]
arr = arr[::-1]

x, y = 5, 5
def abc(level):
    global x, y
    if level == -1:
        return

    if arr[level] == 'up':
        y -= 1
    elif arr[level] == 'down':
        y += 1
    elif arr[level] == 'left':
        x -= 1
    elif arr[level] == 'right':
        x += 1
    else: # click이면
        print(y, x, sep=',')

    abc(level-1)

abc(n-1)

# 아. click이 항상 마지막에 오는게 아니지
# 4
# up
# click
# right
# click
# 이 경우, 
# 4,5
# 4,6
# 이렇게 두 줄 출력!
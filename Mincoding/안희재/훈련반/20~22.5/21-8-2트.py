n = int(input())
arr = [input() for _ in range(n)]
# n이 level이라고 보면 될듯
arr = arr[::-1]

x, y = 5, 5
def abc(level):
    global x, y
    if level == 0:
        return

    if arr[level] == 'up':
        y -= 1
    elif arr[level] == 'down':
        y += 1
    elif arr[level] == 'left':
        x -= 1
    else:
        x += 1

    abc(level-1)

abc(n-1)
print(y, x, sep=',')

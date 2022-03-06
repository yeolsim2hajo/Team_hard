# 생일선물로 마우스를 만들고 고백할라항다
# 마우스는 5,5 에 위치
# up y-> -1
# down y-> +1
# left x -1
# right  x + 1
#click 는 현재 위치출력

y = 5
x = 5
n = int(input())
cmd = []
for i in range(n):
    cmd.append(input())

for k in range(n):
    if cmd[k] == 'up':
        y = y - 1
    if cmd[k] == 'down':
        y = y + 1 
    if cmd[k] == 'right':
        x = x + 1
    if cmd[k] == 'left':
        x = x - 1
    if cmd[k] == 'click':
        print('{},{}'.format(y, x))
        

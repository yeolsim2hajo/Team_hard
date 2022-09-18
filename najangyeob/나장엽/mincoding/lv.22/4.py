moving = list(input() for _ in range(5))
position = 1

for i in range(len(moving)):
    if moving[i] == 'up':
        position += 1
    if moving[i] == 'down':
        position -= 1
        
    if position == 0:
        if moving[i] == 'down':
            position -= 1
        if moving[i] == 'up':
            position += 1
        
if position > 0:
    print(position)
else:
    print('B{}'.format(-position))
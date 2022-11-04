#221104
start, end = map(int, input().split())
while not (2 <= start <= 9) or not (2 <= end <= 9):
    print('INPUT ERROR!')
    start, end = map(int, input().split())
step = -1 if start > end else 1
for i in range(1,10):
    for j in range(start, end+step, step):
        result = i*j
        if result < 10:
            result = f' {i * j}'
        print(f'{j} * {i} = {result}', end='   ')
    print()
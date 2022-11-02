#221102
result = ['E', 'A', 'B', 'C', 'D']
for _ in range(3):
    game = input().split()
    print(result[game.count('0')])


result = ['E', 'A', 'B', 'C', 'D']
for _ in range(3):
    index = input().split().count('0')
    print(result[index])

result = ['E', 'A', 'B', 'C', 'D']
for _ in range(3):
    game = input().split()
    index = 0
    for element in game:
        if element == '0':
            index += 1
    print(result[index])
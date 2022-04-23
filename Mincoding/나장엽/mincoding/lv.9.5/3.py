arr = [
    ['D','A','A'],
    ['B','C','D'],
    ['E','F','A'],
    ['A','A','D'],
    ['F','G','E']
]

str = input()

for i in range(len(arr)):
    for k in range(len(arr[i])):
        if arr[i][k] == str:
            print(f'({i},{k})')
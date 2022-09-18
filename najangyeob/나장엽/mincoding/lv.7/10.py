str = input()

arr = [[str]*4 for _ in range(4)]

for i in arr:
    print(''.join(i))
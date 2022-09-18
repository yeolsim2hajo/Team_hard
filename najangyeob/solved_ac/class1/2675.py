T = int(input())

for tc in range(T):
    R, target = input().split()
    R = int(R)
    i = 0
    while True:
        if i == len(target):
            break

        print(target[i]*R, end= '')
        i += 1
    print()
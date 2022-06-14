num = int(input())
a = []
for i in range(num):
    [x, y] = map(int, input().split())
    rev = [y, x]
    a.append(rev)
b = sorted(a)
for i in range(num):
    print(b[i][1], b[i][0])
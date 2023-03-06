#230306
check = [set(), set()]
for _ in range(3):
    position = list(map(int, input().split()))
    for i in range(2):
        key = position[i]
        if key in check[i]:
            check[i].remove(key)
        else:
            check[i].add(key)
print(*check[0], *check[1])
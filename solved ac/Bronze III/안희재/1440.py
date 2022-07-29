from itertools import permutations
perms = list(permutations(map(int, input().split(":"))))
count = 0
for a, b, c in perms:
    if 1 <= a <= 12 and 0 <= b <= 59 and 0 <= c <= 59:
        count += 1
print(count)
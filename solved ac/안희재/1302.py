import sys
book = dict()
n = int(input())
for _ in range(n):
    name = sys.stdin.readline().rstrip()
    if name in book:
        book[name] += 1
    else:
        book[name] = 1
max = 0
sbook = dict(sorted(book.items()))
for i in sbook:
    if (sbook[i]) > max:
        max = sbook[i]
        maxi = i
print(maxi)
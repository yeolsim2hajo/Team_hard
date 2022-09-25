now = max_people = 0
for _ in range(4):
    off, on  = map(int, input().split())
    now -= off - on
    max_people = max(now, max_people)
print(max_people)

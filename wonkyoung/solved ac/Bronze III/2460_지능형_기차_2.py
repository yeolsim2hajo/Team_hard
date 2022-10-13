max_people = now = 0
for _ in range(10):
    get_off, board = map(int, input().split())
    now += board - get_off
    max_people = max(max_people, now)
print(max_people)
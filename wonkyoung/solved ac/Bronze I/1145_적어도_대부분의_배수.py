#220923
five = list(map(int, input().split()))
min_number = 1e10
path = []
def select(level, multiple):
    global min_number
    if level == 3:
        limit = min(path)
        common = 1
        for i in range(limit, 1, -1):
            cnt = 0
            for j in range(3):
                if path[j]%i == 0:
                   cnt += 1
            if cnt >= 2:
                common *= i
                

        min_number = multiple
        return
    for number in five:
        path.append(number)
        select(level+1, multiple*number)
        path.pop()
select(0,1)
print(min_number)

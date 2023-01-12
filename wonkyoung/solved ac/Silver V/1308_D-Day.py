#221013
today = list(map(int, input().split()))
camp = list(map(int, input().split()))
numbers = [1000, 0, 0]
wait = False
for i in range(3):
    if camp[i] - today[i] == numbers[i]:
        wait = True
        continue
    else:
        wait = False
        if camp[i] - today[i] > numbers[i]:
            print('gg')
        break

if wait:
    print('gg')
else:
    left = 0
    months = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31,
              8:31, 9:30, 10:31, 11:30, 12:31}
    def is_leap_year(year):
        global left
        if year%400 == 0:
            return 1
        elif year%100 and i%4 == 0:
            return 1
        return 0

    for i in range(today[0]+1, camp[0]):
        left += 365 + is_leap_year(i)

    if is_leap_year(today[0]) and today[1] <= 2:
        left += 1

    for i in range(today[1]+1, 13):
        left += months[i]

    for i in range(1, camp[1]):
        left += months[i]

    left += months[today[1]] - today[2]
    left += camp[2]

    print(f'D-{left}')


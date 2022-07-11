# 시작하는 시각과, 오븐 구이를 하는데 필요한 시간이 분단위로 주어졌을 때, 오븐구이가 끝나는 시각을 계산하는 프로그램을 작성하라
# 첫 째 줄에는 현재 시각 -> 시(a) 와 분(b)이  정수로 빈칸을 두고 주어진다
# 두 번째 줄에는 요리하는데 필요한 시간 c가 분단위로 주어진다



a, b = map(int, input().split())
c = int(input())


hour = a
minute = b + c
if minute >= 60: # b + c가 60분을 넘어가면 다시 0 ~ 60 사이의 값을 가지게 된다. 
    over_hour = minute // 60 # 60분이 넘어갔을 때, 몫을 할당
    minute = minute % 60 # 40 + 80 -> 120 % 60 -> 0 # minute는 % 연산을 이용하여 나머지를 할당

    if over_hour + hour >= 24:  # 또한 over_hour + hour이 24시를 넘어가게 되면 다시 0부터  24를 반복하게 된다.
        dawn = (over_hour + hour) % 24 # % 연산을 이용하여 dawn에 할당
        print(dawn, minute)  # 24시를 넘어가게 되는 경우 출력
    else: # 24시를 넘어가지 않는 경우 
        print(hour + over_hour, minute)

else: # 그 외의 모든 경우 (24시를 넘지고 않고, 60분을 넘지도 않는 경우
    print(hour, minute)
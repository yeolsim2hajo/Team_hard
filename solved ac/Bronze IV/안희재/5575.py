# 출/퇴근 시간 각각 초로 환산해서 빼주고,
# 60을 나눈 몫을 시에, 나머지를 다시 60으로 나누고 ...

for i in range(3):
    lst = list(map(int, input().split()))
    start = lst[0:3]
    end = lst[3:6]
    start_sum = 3600*lst[0] + 60*lst[1] + lst[2]
    end_sum = 3600*lst[3] + 60*lst[4] + lst[5]

    work_time = end_sum - start_sum
    hour = work_time // 3600
    minute = work_time % 3600 // 60
    second = work_time % 3600 % 60
    
    print(hour, minute, second)
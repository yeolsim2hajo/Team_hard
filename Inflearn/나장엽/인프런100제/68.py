lst = list(input().split())
n = input()
for i in range(len(lst)):
    if int(lst[i][:2]) < int(n[:2]):
        print("지나갔습니다", end=" ")
    elif int(lst[i][:2]) == int(n[:2]):
        if int(lst[i][3:]) < int(n[3:]):
            print("지나갔습니다", end=" ")
        else:
            print(f"0시간 {int(lst[i][3:])-int(n[3:])}분", end=" ")
    else:
        if int(lst[i][3:]) < int(n[3:]):
            print(f"{int(lst[i][:2])-int(n[:2])-1}시간 {60 + int(lst[i][3:])-int(n[3:])}분", end=" ")
        else:
            print(f"{int(lst[i][:2])-int(n[:2])}시간 {int(lst[i][3:])-int(n[3:])}분", end=" ")



bus = input().split()
now = list(map(int, input().split(':')))
answer = []
for time in bus:
    time_sp = list(map(int,time.split(':')))
    total_minute = (time_sp[0]-now[0]) * 60 + time_sp[1]-now[1]
    if total_minute < 0:
        answer.append('지나갔습니다')
    else:
        hour, minute = divmod(total_minute,60)
        print(hour, minute)
        if hour >= 10 and minute >= 10:
            answer.append('{}시간 {}분'.format(hour, minute))
        elif hour >= 10:
            answer.append('{}시간 0{}분'.format(hour, minute))
        elif minute >= 10:
            answer.append('0{}시간 {}분'.format(hour, minute))
        else:
            answer.append('0{}시간 0{}분'.format(hour, minute))
print(answer)
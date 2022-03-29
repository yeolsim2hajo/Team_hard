# 기존의 내 코드 너무 별로 -> 레퍼런스처럼 하기. 매우 깔끔
# split, zfill, 함수 사용
    # 특히, 00표현하려고 if문 줬는데 ㅠㅠㅠ;;;
arr = input()
now = input()

def sol(tb, rt):
    answer = []
    rt = rt.split(':')
    for i in range(len(tb)):
        time = tb[i].split(':')
        time_to_min = ((int(time[0])*60 + int(time[1])) - (int(rt[0])*60+int(rt[1])))
        if time_to_min < 0:
            answer.append("지나갔습니다")
        else:
            a = (time_to_min) // 60
            b = (time_to_min) % 60
            answer.append(str(a).zfill(2)+'시간 '+str(b).zfill(2)+'분')
    return answer

sol(arr,now)
# sol(["12:30", "13:20", "14:13"], "12:40")
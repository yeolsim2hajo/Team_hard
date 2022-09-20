# 1. 각 차량의 "총" 주차시간 구하기
    # 이때, IN만 있을 경우, 자동으로 23:59에 나간 처리(예외)
# 2. 주차요금 정산하기(최소시간 넘으면 계산 다시)

import math
from collections import defaultdict # 값을 주지 않으면, default값을 자동으로 매겨줌(에러방지 가능)

def solution(fees, records):
    answer = []

    car_dict = {}
    total_times = defaultdict(int) # 차가 주자창에 머문 시간을 car_dict로

    for record in records : # records를 순회해서 각 머문시간 계산
        time, car, order = record.split() # 입출 시간, 차 넘버, In or Out ## 여기서 order는 쓰지는 않음
        hour, minutes = time.split(":") # 10:52 -> [10,52]
        toMinute = int(hour) * 60 + int(minutes) # 분으로 환산
        if car in car_dict : # 차가 이미 들어가 있다면(이전에 입장했음) => out한다는 뜻
            total_times[car] += toMinute - car_dict[car] # 시간 계산
            del car_dict[car] # 리스트에서 지워주기
        else : # 만약 차가 리스트에 없다면 => in한다는 뜻
            car_dict[car] = toMinute

    # 예외상황: in한 경우만 있음
    for car, remain in car_dict.items():
        total_times[car] += 1439 - remain # 1439 = 60*23 + 59

    # 총 요금 정산
    default_times, base_rate, unit_time, unit_fee = fees # 기본시간 / 기본요금 / 단위시간 / 단위요금
    for car, remain in total_times.items() :
        total_charge = base_rate
        if remain > default_times : # 만약, 기본시간을 넘는다면 추가요금 징수
            total_charge += math.ceil((remain - default_times) / unit_time) * unit_fee # 올림 처리
        answer.append((car, total_charge))

    # 오름차순 정렬후 출력
    answer.sort()
    return [value[1] for value in answer]
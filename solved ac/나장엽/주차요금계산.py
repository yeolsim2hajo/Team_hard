import math 
def solution(fees, records) : 
    check = dict() # in, out check
    fee = dict() # 요금 계산 해쉬

    for record in records:
        parking_time, car_number, InOut = record.split()
        hour, minute = parking_time.split(':')

        # 계산된 누적 주차 시간
        convert_time = int(hour) * 60 + int(minute)

        if InOut == 'IN':
            check[car_number] = convert_time

        else: # 출차 시 요금을 계산하여 fee 해쉬에 저장
            fee[car_number] = fee.get(car_number, 0) + (convert_time - check[car_number]) # 값이 없으면 0을 반환하기 위해 get 메서드에 option값으로 0을 설정
            del check[car_number] # 삭제(출차)

    for chk in check: # 입차된 후 출차 내역이 없는 경우는 check 배열에 저장되어 있다.
        fee[chk] =  fee.get(chk, 0) + (23 * 60) + 59 - check[chk] # 23:59을 기준으로 요금 계산.

    answer = []
    
    for car_number, fee_time in sorted(fee.items()): 
        if fee_time > fees[0]: # 기본 시간을 초과하는 경우,
            answer.append(fees[1] + math.ceil((fee_time - fees[0]) / fees[2]) * fees[3]) # ((기본요금 + 누적시간 - 기본시간) / 단위시간) * 단위 요금
        else: # 기본 시간 초과 x
            answer.append(fees[1])
    return answer

fees = [180, 5000, 10, 600]
records = ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]

print(solution(fees, records))
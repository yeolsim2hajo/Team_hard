import math 

def solution(fees, records) : 
    check = dict()
    fee = dict()

    for record in records:
        time, car_number, InOut = record.split()
        hour, minute = time.split(':')
        convert_time = int(hour) * 60 + int(minute)

        if InOut == 'IN':
            check[car_number] = convert_time

        else:
            fee[car_number] = fee.get(car_number, 0) + (convert_time - check[car_number]) # 값이 없으면 0을 반환하기 위해 get 메서드에 option값으로 0을 설정
            del check[car_number] # 삭제

    for chk in check:
        fee[chk] =  fee.get(chk, 0) + (23 * 60) + 59 - check[chk]

    answer = []
    for car_number, fee_time in sorted(fee.items()):
        if fee_time > fees[0]:
            answer.append(fees[1] + math.ceil((fee_time - fees[0]) / fees[2]) * fees[3])
        else:
            answer.append(fees[1])
    return answer

fees = [180, 5000, 10, 600]
records = ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]

print(solution(fees, records))
# def solution(fees, records):
#     from collections import defaultdict
#     duration = defaultdict(int)
#     car_info = {}
#     for record in records:
#         time_stamp, number, now = record.split()
#         hour, minute = map(int, time_stamp.split(':'))
#         calc = hour * 60 + minute
#         number = int(number)
#         if now == 'IN':
#             car_info[number] = calc
#         else:
#             duration[number] += calc - car_info[number]
#             car_info[number] = -1
#     end_time = 23*60 + 59
#     for car in car_info.keys():
#         if car_info[car] != -1:
#             duration[car] += end_time - car_info[car]
#     keys = sorted(duration)
#     answer = []
#     for key in keys:
#         cost = fees[1] if duration[key] <= fees[0] else fees[1] + ((duration[key] - fees[0] -1)//fees[2] + 1) * fees[3]
#         answer.append(cost)
#     return answer
# print(solution([180, 5000, 10, 600], ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]))
# print(solution([1, 461, 1, 10], ["00:00 1234 IN"]))
'''
테스트 1 〉	통과 (0.05ms, 10.3MB)
테스트 2 〉	통과 (0.03ms, 10.3MB)
테스트 3 〉	통과 (0.05ms, 10.3MB)
테스트 4 〉	통과 (0.08ms, 10.4MB)
테스트 5 〉	통과 (0.16ms, 10.3MB)
테스트 6 〉	통과 (0.18ms, 10.4MB)
테스트 7 〉	통과 (1.55ms, 10.5MB)
테스트 8 〉	통과 (0.87ms, 10.3MB)
테스트 9 〉	통과 (0.17ms, 10.4MB)
테스트 10 〉	통과 (1.38ms, 10.3MB)
테스트 11 〉	통과 (2.26ms, 10.4MB)
테스트 12 〉	통과 (2.37ms, 10.5MB)
테스트 13 〉	통과 (0.06ms, 10.3MB)
테스트 14 〉	통과 (0.04ms, 10.4MB)
테스트 15 〉	통과 (0.04ms, 10.2MB)
테스트 16 〉	통과 (0.03ms, 10.3MB)
'''


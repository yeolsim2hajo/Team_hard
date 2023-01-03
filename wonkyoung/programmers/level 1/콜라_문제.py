#221029
def solution(empty_bottle, cola, my_bottle):
    answer = 0
    while True:
        # 몫
        quot = my_bottle//empty_bottle
        if quot == 0:
            return answer
        # 교환된 콜라
        exchanged_cola = quot * cola
        answer += exchanged_cola
        my_bottle = my_bottle%empty_bottle + exchanged_cola
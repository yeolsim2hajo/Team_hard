#230107
# def solution(k, m, score):
#     answer = index = 0
#     score.sort(reverse=True)
#     length = len(score)
#     while True:
#         end = index + m - 1
#         if end >= length:
#             break
#         answer += score[end] * m
#         index = end + 1
#     return answer


# k 사용
def solution(k, m, score):
    answer = 0
    numbers = [0] * (k+1)
    for i in score:
        numbers[i] += 1
    large_cnt = 0
    for i in range(k, 0, -1):
        large_cnt += numbers[i]
        if large_cnt >= m:
            answer += (large_cnt//m) * i * m
            large_cnt %= m
        # print(numbers, answer)
    return answer
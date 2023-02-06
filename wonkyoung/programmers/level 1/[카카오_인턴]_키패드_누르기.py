#230122
# 다시 시도 해보자
# def solution(numbers, hand):
#     answer = ''
#     right, left = {1, 4, 7}, {3, 6, 9}
#
#     now_right, now_left = '#', '*'
#     for number in numbers:
#         if number in right:
#             answer += 'R'
#         elif number in left:
#             answer += 'L'
#         elif number:
#
#         else:
#             pass
#     return answer


#230206
def solution(numbers, hand):
    answer = ''
    position = [(3, 0), (3, 2)]
    for number in numbers:
        move_to = divmod(number-1, 3) if number else (3, 1)
        y = move_to[1]
        if y == 2:
            answer += 'R'
            position[1] = move_to[:]
        elif y == 0:
            answer += 'L'
            position[0] = move_to[:]
        else:
            dif = lambda a, b: abs(a-b)
            left_dist = sum(map(dif, position[0], move_to[:]))
            right_dist = sum(map(dif, position[1], move_to[:]))
            if left_dist > right_dist:
                position[1] = move_to[:]
                answer += 'R'
            elif left_dist < right_dist:
                position[0] = move_to[:]
                answer += 'L'
            elif hand == 'left':
                position[0] = move_to[:]
                answer += 'L'
            else:
                position[1] = move_to[:]
                answer += 'R'
    return answer
'''
테스트 1 〉	통과 (0.00ms, 10.2MB)
테스트 2 〉	통과 (0.01ms, 10.3MB)
테스트 3 〉	통과 (0.01ms, 10.3MB)
테스트 4 〉	통과 (0.00ms, 10.3MB)
테스트 5 〉	통과 (0.01ms, 10.3MB)
테스트 6 〉	통과 (0.01ms, 10.3MB)
테스트 7 〉	통과 (0.01ms, 10.2MB)
테스트 8 〉	통과 (0.02ms, 10.2MB)
테스트 9 〉	통과 (0.02ms, 10.2MB)
테스트 10 〉	통과 (0.03ms, 10.2MB)
테스트 11 〉	통과 (0.07ms, 10.2MB)
테스트 12 〉	통과 (0.03ms, 10.3MB)
테스트 13 〉	통과 (0.09ms, 10.3MB)
테스트 14 〉	통과 (0.18ms, 10.2MB)
테스트 15 〉	통과 (0.33ms, 10.2MB)
테스트 16 〉	통과 (1.01ms, 10.1MB)
테스트 17 〉	통과 (1.18ms, 10.1MB)
테스트 18 〉	통과 (1.09ms, 10.1MB)
테스트 19 〉	통과 (1.24ms, 10.2MB)
테스트 20 〉	통과 (1.13ms, 10.2MB)
'''

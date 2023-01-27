#230127
# def solution(dots):
#     answer = 1
#     x, y = dots[0]
#     for i in range(1,3):
#         nx, ny = dots[i]
#         if x != nx and y != ny:
#             return abs(x-nx) * abs(y-ny)
#         elif x != nx:
#             answer *= abs(x-nx)
#         else:
#             answer *= abs(y-ny)
#     return answer


#
def solution(dots):
    answer = 1
    x, y = dots[0]
    for i in range(1,3):
        nx, ny = dots[i]
        dif_x, dif_y = abs(x-nx), abs(y-ny)
        if dif_x and dif_y:
            return dif_x * dif_y
        elif dif_x:
            answer *= dif_x
        else:
            answer *= dif_y
    return answer
'''
테스트 1 〉	통과 (0.00ms, 10.1MB)
테스트 2 〉	통과 (0.00ms, 10.2MB)
테스트 3 〉	통과 (0.00ms, 10.2MB)
테스트 4 〉	통과 (0.00ms, 10.1MB)
테스트 5 〉	통과 (0.01ms, 10.1MB)
'''

def solution(dots):
    answer = 1
    def abs_dif(num1, num2):
        return abs(num1-num2)
    for i in range(1,3):
        dif_x, dif_y = map(abs_dif,dots[0], dots[i])
        if dif_x and dif_y:
            return dif_x * dif_y
        elif dif_x:
            answer *= dif_x
        else:
            answer *= dif_y
    return answer
'''
테스트 1 〉	통과 (0.01ms, 10.3MB)
테스트 2 〉	통과 (0.01ms, 10.2MB)
테스트 3 〉	통과 (0.01ms, 10.3MB)
테스트 4 〉	통과 (0.01ms, 10.3MB)
테스트 5 〉	통과 (0.01ms, 10.2MB)
'''
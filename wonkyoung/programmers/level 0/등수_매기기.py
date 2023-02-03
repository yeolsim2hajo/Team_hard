#230202
def solution(score):
    length = len(score)
    sorted_result = [[sum(score[i])//2, length-i] for i in range(length)]
    sorted_result.sort()
    answer = [0] * length
    answer[sorted_result[0][1]] = 1
    cnt = 0
    for i in range(1, length):
        avg, j = sorted_result[i]
        if sorted_result[i-1][0] == avg:
            sorted_result[i][1] = sorted_result[i-1][1]
            answer[j-1] = i-cnt
            cnt += 1
        else:
            answer[j-1] = i+1
            cnt = 0
    return answer
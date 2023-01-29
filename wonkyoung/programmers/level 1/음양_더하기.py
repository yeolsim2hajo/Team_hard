# 220906
# 더 빠름
def solution(absolutes, signs):
    answer = 0
    length = len(signs)
    for i in range(length):
        if signs[i]:
            answer += absolutes[i]
        else:
            answer -= absolutes[i]
    return answer

# 새로운 시도 - 더 느림
def solution(absolutes, signs):
    answer = 0
    length = len(signs)
    for i in range(length):
        answer -= absolutes[i] * (-1) ** (signs[i])
    return answer

#230129
def solution(absolutes, signs):
    answer = 0
    length = len(signs)
    for i in range(length):
        answer += absolutes[i] if signs[i] else -absolutes[i]
    return answer
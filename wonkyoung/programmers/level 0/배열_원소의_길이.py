#230207
# map 사용
def solution(strlist):
    answer = list(map(lambda x:len(x), strlist))
    return answer

# for문 + map
def solution(strlist):
    answer = []
    for element in strlist:
        answer.append(len(element))
    return answer

# for문 * 2
def solution(strlist):
    answer = []
    for element in strlist:
        cnt = 0
        for _ in element:
            cnt += 1
        answer.append(cnt)
    return answer

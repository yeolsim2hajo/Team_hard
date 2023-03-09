#230309
def solution(msg):
    answer = []
    dictionary = {chr(64+i):i for i in range(1, 27)}
    next_num = 27
    length = len(msg)
    start = 0
    while True:
        element = msg[start]
        num = dictionary[element]
        for end in range(start+1, length):
            element += msg[end]
            if dictionary.get(element):
                num = dictionary[element]
            else:
                dictionary[element] = next_num
                next_num += 1
                break
        else:
            answer.append(num)
            break
        start = end
        answer.append(num)
    return answer
# print(solution('KAKAO'))
# print(solution('TOBEORNOTTOBEORTOBEORNOT'))
'''
테스트 1 〉	통과 (0.02ms, 10.1MB)
테스트 2 〉	통과 (0.02ms, 10.4MB)
테스트 3 〉	통과 (0.01ms, 10.4MB)
테스트 4 〉	통과 (0.18ms, 10.4MB)
테스트 5 〉	통과 (0.02ms, 10.2MB)
테스트 6 〉	통과 (0.27ms, 10.2MB)
테스트 7 〉	통과 (0.39ms, 10.2MB)
테스트 8 〉	통과 (0.26ms, 10.4MB)
테스트 9 〉	통과 (0.01ms, 10.2MB)
테스트 10 〉	통과 (0.26ms, 10.2MB)
테스트 11 〉	통과 (0.19ms, 10.2MB)
테스트 12 〉	통과 (0.45ms, 10.4MB)
테스트 13 〉	통과 (0.38ms, 10.2MB)
테스트 14 〉	통과 (0.40ms, 10.1MB)
테스트 15 〉	통과 (0.39ms, 10.3MB)
테스트 16 〉	통과 (0.56ms, 10.2MB)
테스트 17 〉	통과 (0.31ms, 10.2MB)
테스트 18 〉	통과 (0.10ms, 10.2MB)
테스트 19 〉	통과 (0.12ms, 10.2MB)
테스트 20 〉	통과 (0.44ms, 10.2MB)
'''
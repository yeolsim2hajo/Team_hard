def solution(s):
    answer = 0
    numbers = ['zero', 'one', 'two', 'three','four', 'five', 'six', 'seven', 'eight', 'nine']
    match = {numbers[i]:i for i in range(10)}
    length = len(s)
    index = 0
    while index < length:
        answer *= 10
        if s[index].isdigit():
            answer += int(s[index])
            index += 1
        else:
            key = s[index:index+3]
            for end in range(3, 6):
                print(index, key)
                if match.get(key, -1) != -1:
                    answer += match[key]
                    break
                key += s[index+end]
            index += end
    print(answer)
    return answer
solution("one4seveneight")
solution("23four5six7")
'''
테스트 1 〉	통과 (0.01ms, 10.2MB)
테스트 2 〉	통과 (0.03ms, 10.2MB)
테스트 3 〉	통과 (0.04ms, 10.3MB)
테스트 4 〉	통과 (0.04ms, 10.3MB)
테스트 5 〉	통과 (0.03ms, 10.3MB)
테스트 6 〉	통과 (0.04ms, 10.3MB)
테스트 7 〉	통과 (0.03ms, 10.2MB)
테스트 8 〉	통과 (0.04ms, 10.4MB)
테스트 9 〉	통과 (0.05ms, 10MB)
테스트 10 〉	통과 (0.03ms, 10.3MB)
'''



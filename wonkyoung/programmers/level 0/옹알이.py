#221023
def solution(babbling):
    answer = 0
    possible = {'aya', 'ye', 'woo', 'ma'}
    for word in babbling:
        if word in possible:
            answer += 1
        else:
            plus_word = ''
            new_word = word
            for element in possible:
                if element in new_word:
                    plus_word += element
                    new_word.split()
            if len(plus_word) == len(word):
                answer += 1

    return answer

print(solution(["aya", "yee", "u", "maa"]))
print(solution(["ayaye", "uuu", "yeye", "yemawoo", "ayaayaa"]))


#??
def solution(babbling):
    answer = 0
    possible = {'aya', 'ye', 'woo', 'ma'}
    for word in babbling:
        if word in possible:
            answer += 1
        else:
            plus_word = ''
            for element in possible:
                if element in word:
                    plus_word += element
            if len(plus_word) == len(word):
                answer += 1

    return answer
'''
테스트 1 〉	통과 (0.03ms, 10MB)
테스트 2 〉	통과 (0.05ms, 10.2MB)
테스트 3 〉	통과 (0.05ms, 10.1MB)
테스트 4 〉	통과 (0.06ms, 9.98MB)
테스트 5 〉	통과 (0.06ms, 10.3MB)
테스트 6 〉	통과 (0.04ms, 10.3MB)
테스트 7 〉	통과 (0.04ms, 10.3MB)
테스트 8 〉	통과 (0.07ms, 10.1MB)
테스트 9 〉	통과 (0.02ms, 9.95MB)
테스트 10 〉	통과 (0.03ms, 10.1MB)
테스트 11 〉	통과 (0.01ms, 10MB)
테스트 12 〉	통과 (0.00ms, 10MB)
'''

#230104
def solution(babbling):
    answer = 0
    possible = {'a':['aya', 3],
                'y':['ye', 2],
                'w':['woo', 3],
                'm':['ma', 2]}
    for word in babbling:
        index = 0
        while index < len(word):
            alp = word[index]
            if possible.get(alp):
                sound, length = possible[alp]
                if sound == word[index:index+length]:
                    index += length
                else:
                    break
            else:
                break
        else:
            answer += 1
    return answer
'''
테스트 1 〉	통과 (0.04ms, 10.1MB)
테스트 2 〉	통과 (0.08ms, 10MB)
테스트 3 〉	통과 (0.01ms, 10.2MB)
테스트 4 〉	통과 (0.05ms, 10.3MB)
테스트 5 〉	통과 (0.02ms, 10.2MB)
테스트 6 〉	통과 (0.04ms, 10.1MB)
테스트 7 〉	통과 (0.03ms, 10.2MB)
테스트 8 〉	통과 (0.06ms, 10.2MB)
테스트 9 〉	통과 (0.04ms, 10.3MB)
테스트 10 〉	통과 (0.03ms, 10.2MB)
테스트 11 〉	통과 (0.02ms, 10.1MB)
테스트 12 〉	통과 (0.01ms, 10.1MB)
'''
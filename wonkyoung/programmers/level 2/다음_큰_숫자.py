#230214
def solution(n):
    def conv_binary(num):
        answer = []
        while num:
            remain = num % 2
            answer.append(remain)
            num //= 2
        return answer

    def conv_decimal(num_list):
        answer = 0
        multiple = 1
        for num in num_list:
            answer += multiple * num
            multiple *= 2
        return answer

    def transform_now():
        now = conv_binary(n)
        length, one = len(now), 0
        passed_one = False
        for i in range(length):
            if now[i] == 1:
                passed_one = True
                one += 1
            elif passed_one:
                now[i], now[i - 1] = now[i - 1], now[i]
                one -= 1
                limit = i - 1
                break
        else:
            now.append(1)
            now[-2] = 0
            limit = length - 1
            one -= 1
        now[:limit] = [1] * one + [0] * (limit - one)
        return conv_decimal(now)

    return transform_now()
'''
정확성  테스트
테스트 1 〉	통과 (0.01ms, 10.3MB)
테스트 2 〉	통과 (0.01ms, 10.4MB)
테스트 3 〉	통과 (0.01ms, 10.2MB)
테스트 4 〉	통과 (0.01ms, 10.3MB)
테스트 5 〉	통과 (0.01ms, 10.3MB)
테스트 6 〉	통과 (0.01ms, 10.3MB)
테스트 7 〉	통과 (0.01ms, 10.2MB)
테스트 8 〉	통과 (0.01ms, 10.1MB)
테스트 9 〉	통과 (0.01ms, 10.3MB)
테스트 10 〉	통과 (0.01ms, 10.2MB)
테스트 11 〉	통과 (0.01ms, 10.4MB)
테스트 12 〉	통과 (0.01ms, 10.2MB)
테스트 13 〉	통과 (0.01ms, 10.3MB)
테스트 14 〉	통과 (0.01ms, 10.2MB)
효율성  테스트
테스트 1 〉	통과 (0.03ms, 10.3MB)
테스트 2 〉	통과 (0.02ms, 10.3MB)
테스트 3 〉	통과 (0.02ms, 10.4MB)
테스트 4 〉	통과 (0.02ms, 10.2MB)
테스트 5 〉	통과 (0.03ms, 10.2MB)
테스트 6 〉	통과 (0.02ms, 10.2MB)
'''
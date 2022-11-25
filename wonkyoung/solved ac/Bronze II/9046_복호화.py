#221125

# 80
# T = int(input())
# for _ in range(T):
#     sentence = input().replace(' ', '')
#     match = {}
#     for alp in sentence:
#         if match.get(alp):
#             match[alp] += 1
#         else:
#             match[alp] = 1
#     max_cnt = 0
#     answer = '?'
#     for key, value in match.items():
#         if value > max_cnt:
#             max_cnt = value
#             answer = key
#         elif value == max_cnt:
#             answer = '?'
#     print(answer)


# 함수화 => 시간 더 걸림 - 88
# T = int(input())

# def fill_match():
#     for alp in sentence:
#         if match.get(alp):
#             match[alp] += 1
#         else:
#             match[alp] = 1

# def return_answer():
#     max_cnt, answer = 0, '?'
#     for key, value in match.items():
#         if value > max_cnt:
#             max_cnt = value
#             answer = key
#         elif value == max_cnt:
#             answer = '?'
#     return answer

# for _ in range(T):
#     sentence = input().replace(' ', '')
#     match = {}
#     fill_match()
#     print(return_answer())


# main 사용 - 84 => 80

def fill_match(sentence):
    match = {}
    for alp in sentence:
        if match.get(alp):
            match[alp] += 1
        else:
            match[alp] = 1
    return match

def return_answer(match):
    max_cnt, answer = 0, '?'
    for key, value in match.items():
        if value > max_cnt:
            max_cnt = value
            answer = key
        elif value == max_cnt:
            answer = '?'
    return answer

def main():
    T = int(input())
    for _ in range(T):
        sentence = input().replace(' ', '')
        match = fill_match(sentence)
        print(return_answer(match))
main()


# 함수 안의 함수 - 84

def main():
    T = int(input())

    def fill_match():
        match = {}
        for alp in sentence:
            if match.get(alp):
                match[alp] += 1
            else:
                match[alp] = 1
        return match

    def return_answer():
        max_cnt, answer = 0, '?'
        for key, value in match.items():
            if value > max_cnt:
                max_cnt = value
                answer = key
            elif value == max_cnt:
                answer = '?'
        return answer
    
    for _ in range(T):
        sentence = input().replace(' ', '')
        match = fill_match()
        print(return_answer())
main()
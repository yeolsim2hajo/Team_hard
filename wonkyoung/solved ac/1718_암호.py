#221204
# sentence = input()
# code = input()
# a = ord('a')
# match = {}
# for i in range(26):
#     key, value = chr(i + a), i+1
#     match[key] = value
#     match[value] = key
# length, code_len = len(sentence), len(code)
# answer = ''
# if length <= code_len:
#     for i in range(length):
#         alp, code_alp = sentence[i], code[i]
#         if alp != ' ':
#             key = (match[alp] - match[code_alp] - 1)%26 + 1
#             if not (1 <= key <= 26):
#                 answer += match[key+26]
#             else:
#                 answer += match[key]
#         else:
#             answer += ' '
# else:
#     for i in range(length):
#         alp, code_alp = sentence[i], code[i%code_len]
#         if alp != ' ':
#             key = (match[alp] - match[code_alp] - 1)%26 + 1
#             if not (1 <= key <= 26):
#                 answer += match[key+26]
#             else:
#                 answer += match[key]
#         else:
#             answer += ' '
# print(answer)



#
# def conv_sentence():
#     sentence = input()
#     code = input()
#     a = ord('a')
#     match = {}
#     for i in range(26):
#         key, value = chr(i + a), i+1
#         match[key] = value
#         match[value] = key
#
#     length, code_len = len(sentence), len(code)
#     answer = ''
#     if length <= code_len:
#         for i in range(length):
#             alp, code_alp = sentence[i], code[i]
#             if alp != ' ':
#                 key = (match[alp] - match[code_alp] - 1)%26 + 1
#                 if not (1 <= key <= 26):
#                     answer += match[key+26]
#                 else:
#                     answer += match[key]
#             else:
#                 answer += ' '
#     else:
#         for i in range(length):
#             alp, code_alp = sentence[i], code[i%code_len]
#             if alp != ' ':
#                 key = (match[alp] - match[code_alp] - 1)%26 + 1
#                 if not (1 <= key <= 26):
#                     answer += match[key+26]
#                 else:
#                     answer += match[key]
#             else:
#                 answer += ' '
#     return answer
# print(conv_sentence())


#
def conv_sentence():
    sentence = input()
    code = input()
    a = ord('a')
    match = {}
    for i in range(26):
        key, value = chr(i + a), i+1
        match[key] = value
        match[value] = key

    def find_answer():
        length, code_len = len(sentence), len(code)
        answer = ''

        for i in range(length):
            alp, code_alp = sentence[i], code[i%code_len]
            if alp != ' ':
                key = (match[alp] - match[code_alp] - 1)%26 + 1
                if not (1 <= key <= 26):
                    answer += match[key+26]
                else:
                    answer += match[key]
            else:
                answer += ' '
        return answer
    print(find_answer())

conv_sentence()


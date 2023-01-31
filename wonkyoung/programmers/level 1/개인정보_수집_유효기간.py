#230109
#100%가 아님
# def solution(today, terms, privacies):
#     answer = []
#     years = {str(2000+i):2000+i for i in range(23)}
#     months = {str(i).rjust(2, '0'):i for i in range(1, 13)}
#     days = {str(i).rjust(2, '0'):str(i-1 or 28).rjust(2, '0') for i in range(1, 29)}
#     terms_dict = {}
#     for term in terms:
#         alp, number = term.split()
#         terms_dict[alp] = int(number)
#     for i in range(len(privacies)):
#         date, alp = privacies[i].split()
#         after = terms_dict[alp]
#         year, month = divmod(after, 12)
#         date = date.split('.')
#         year += years[date[0]]
#         month += months[date[1]]
#         if month >= 12:
#             year += 1
#             month -= 12
#         day = days[date[2]]
#         if day == '28':
#             month -= 1
#             if month == 0:
#                 month += 12
#                 year -= 1
#         print(year, month, day)
#         new_date = '.'.join([str(year), str(month).rjust(2, '0'), day])
#         if new_date < today:
#             answer.append(i+1)
#     print(answer)
#     return answer

# solution("2022.05.19", ["A 6", "B 12", "C 3"], ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"])

#230131
def solution(today, terms, privacies):
    today = list(map(int, today.split('.')))
    conv_date = lambda date: (date[0]-2000)*28*12 + (date[1] - 1) * 28 + date[2]
    today_num = conv_date(today)
    terms_limit = {}
    for term in terms:
        key, month = term.split()
        terms_limit[key] = today_num - int(month) * 28 + 1
    cnt = 1
    answer = []
    for privacy in privacies:
        date, key = privacy.split()
        if conv_date(list(map(int,date.split('.')))) < terms_limit[key]:
            answer.append(cnt)
        cnt += 1
    return answer
solution("2022.05.19", ["A 6", "B 12", "C 3"], ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"])
'''

테스트 1 〉	통과 (0.03ms, 10.3MB)
테스트 2 〉	통과 (0.04ms, 10.4MB)
테스트 3 〉	통과 (0.03ms, 10.5MB)
테스트 4 〉	통과 (0.04ms, 10.5MB)
테스트 5 〉	통과 (0.06ms, 10.4MB)
테스트 6 〉	통과 (0.04ms, 10.5MB)
테스트 7 〉	통과 (0.04ms, 10.5MB)
테스트 8 〉	통과 (0.04ms, 10.4MB)
테스트 9 〉	통과 (0.07ms, 10.3MB)
테스트 10 〉	통과 (0.08ms, 10.4MB)
테스트 11 〉	통과 (0.08ms, 10.5MB)
테스트 12 〉	통과 (0.13ms, 10.5MB)
테스트 13 〉	통과 (0.13ms, 10.5MB)
테스트 14 〉	통과 (0.10ms, 10.4MB)
테스트 15 〉	통과 (0.09ms, 10.4MB)
테스트 16 〉	통과 (0.13ms, 10.5MB)
테스트 17 〉	통과 (0.14ms, 10.4MB)
테스트 18 〉	통과 (0.14ms, 10.3MB)
테스트 19 〉	통과 (0.24ms, 10.3MB)
테스트 20 〉	통과 (0.14ms, 10.4MB)
'''

# year 범위 변경
def solution(today, terms, privacies):
    today = list(map(int, today.split('.')))
    year = today[0] - 1
    conv_date = lambda date: (date[0] - year) * 28 * 12 + (date[1] - 1) * 28 + date[2]
    today_num = conv_date(today)
    terms_limit = {}
    for term in terms:
        key, month = term.split()
        terms_limit[key] = today_num - int(month) * 28 + 1
    cnt = 1
    answer = []
    for privacy in privacies:
        date, key = privacy.split()
        if conv_date(list(map(int,date.split('.')))) < terms_limit[key]:
            answer.append(cnt)
        cnt += 1
    return answer
'''
테스트 1 〉	통과 (0.03ms, 10.4MB)
테스트 2 〉	통과 (0.04ms, 10.4MB)
테스트 3 〉	통과 (0.03ms, 10.4MB)
테스트 4 〉	통과 (0.03ms, 10.3MB)
테스트 5 〉	통과 (0.04ms, 10.3MB)
테스트 6 〉	통과 (0.04ms, 10.4MB)
테스트 7 〉	통과 (0.05ms, 10.4MB)
테스트 8 〉	통과 (0.07ms, 10.4MB)
테스트 9 〉	통과 (0.08ms, 10.3MB)
테스트 10 〉	통과 (0.10ms, 10.4MB)
테스트 11 〉	통과 (0.08ms, 10.4MB)
테스트 12 〉	통과 (0.14ms, 10.4MB)
테스트 13 〉	통과 (0.15ms, 10.4MB)
테스트 14 〉	통과 (0.09ms, 10.3MB)
테스트 15 〉	통과 (0.09ms, 10.4MB)
테스트 16 〉	통과 (0.14ms, 10.4MB)
테스트 17 〉	통과 (0.22ms, 10.3MB)
테스트 18 〉	통과 (0.24ms, 10.4MB)
테스트 19 〉	통과 (0.15ms, 10.4MB)
테스트 20 〉	통과 (0.14ms, 10.4MB)
'''
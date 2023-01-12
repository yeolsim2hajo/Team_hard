#230109
#100%가 아님
def solution(today, terms, privacies):
    answer = []
    years = {str(2000+i):2000+i for i in range(23)}
    months = {str(i).rjust(2, '0'):i for i in range(1, 13)}
    days = {str(i).rjust(2, '0'):str(i-1 or 28).rjust(2, '0') for i in range(1, 29)}
    terms_dict = {}
    for term in terms:
        alp, number = term.split()
        terms_dict[alp] = int(number)
    for i in range(len(privacies)):
        date, alp = privacies[i].split()
        after = terms_dict[alp]
        year, month = divmod(after, 12)
        date = date.split('.')
        year += years[date[0]]
        month += months[date[1]]
        if month >= 12:
            year += 1
            month -= 12
        day = days[date[2]]
        if day == '28':
            month -= 1
            if month == 0:
                month += 12
                year -= 1
        print(year, month, day)
        new_date = '.'.join([str(year), str(month).rjust(2, '0'), day])
        if new_date < today:
            answer.append(i+1)
    print(answer)
    return answer

solution("2022.05.19", ["A 6", "B 12", "C 3"], ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"])

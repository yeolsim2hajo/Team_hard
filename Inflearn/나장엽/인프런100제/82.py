def math(e):
    flag = 0
    answer = 0

    for i in e:
        if i  == "(":
            flag += 1
        elif i == ")":
            flag -= 1
        if flag != 0:
            answer = False
    if flag == 0:
        answer = True
    return answer  

while 1:
    order = input('데이터 입력(1), 프로그램 종료(2) :')
    if order == '1':
        ex = input('데이터를 입력하세요 :')
        print(math(ex))
    else:
        break


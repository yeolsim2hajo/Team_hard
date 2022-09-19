#83 수학 괄호 파싱 2
# 소괄호, 중괄호 있음
def math(e):
    stack = []
    top = -1
    ans = False
    for element in e:
        if element in {'(','{'}:
            stack.append(element)
            top += 1
        elif element == ')':
            if top != -1:
                conf = stack.pop()
                if conf != '(':
                    break
            else:
                break
        elif element == '}':
            if top != -1:
                conf = stack.pop()
                if conf != '{':
                    break
            else:
                break
    else:
        if stack == []:
            ans = True
    return ans

while 1:
    order = input('데이터 입력(1), 프로그램 종료(2) : ')
    if order == '1':
        ex = input('데이터를 입력하세요 : ')
        print(math(ex))
    else:
        break
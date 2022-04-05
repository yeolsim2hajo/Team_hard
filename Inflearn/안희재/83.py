def math(e):
    m = {
        ')':'(',
        '}':'{',
    }
    stack = []
    for i in e:
        if i in '({':
            stack.append(i)
        elif i in m:
            if len(stack) == 0:
                return False
            else:
                t = m[i]
                if t != stack.pop():
                    return False
    return len(stack) == 0

while 1:
    order = input()
    if order == '1':
        ex = input()
        print(math(ex))
    else:
        break
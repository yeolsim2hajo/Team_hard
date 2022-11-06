#221106
start, end = map(int, input().split())
step = -1 if end < start else 1
def calc_result(answer):
    if answer < 10:
        return f' {answer}'
    return answer
for i in range(start, end+step, step):
    for j in range(3):
        for k in range(1,4):
            print(f'{i} * {3*j+k} = {calc_result(i*(3*j+k))}', end='   ')
        print()
    print()
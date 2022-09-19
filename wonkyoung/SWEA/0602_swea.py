#1865 동철이의 일 분배
# T = int(input())
# def calc(arg=0, total=1):
#     global answer
#     if total == 0:
#         return
#     if total <= answer:
#         return
#     if arg == N:
#         answer = total
#         return
#     for i in range(N):
#         if visited[i] is False:
#             visited[i] = True
#             calc(arg+1, total * work[arg][i])
#             visited[i] = False
# for tc in range(1,1+T):
#     N = int(input())
#     work = []
#     for _ in range(N):
#         work.append(list(map(int,input().split())))
#         for j in range(N):
#             work[-1][j] /= 100
#     answer = 0
#     visited = [False] * N
#     calc()
#     print('#%d %.6f'% (tc, answer*100))


#4311 오래된 스마트폰
T = int(input())
def find_min(total,cnt):
    global min_cnt
    if cnt >= M:
        return
    if min_cnt != -1 and cnt >= min_cnt:
        return
    if target == total:
        min_cnt = cnt
        return
    if total == 0:
        return
    for number in new_numbers:
        for element in calc:
            if element == '1':
                new_total = total + number[0]
            elif element == '2':
                new_total = total - number[0]
            elif number[0] != 1:
                if element == '3':
                    new_total = total * number[0]
                else:
                    new_total = total // number[0]
            else: continue
            if 0 <= new_total < 1000:
                # path.append(element)
                # path.append(number[0])
                if results[new_total] > cnt+number[1]+1:
                    results[new_total] = cnt+number[1]+1
                else: continue
                find_min(new_total, results[new_total])
                # path.pop()
                # path.pop()

def all_numbers(arg=0,total=''):
    if arg and total[0] != '0':
        new_numbers.add((int(total), len(total)))
    if arg == 3:
        return
    for i in numbers:
        all_numbers(arg+1, total+i)

for tc in range(1,1+T):
    N, O, M = map(int, input().split())
    numbers = set(input().split())
    calc = input().split()
    target = input()
    min_cnt = -1
    for number in target:
        if number not in numbers:
            break
    else:
        min_cnt = len(target)
    if min_cnt == -1:
        new_numbers = set()
        all_numbers()
        target = int(target)
        # path = []
        new_numbers = sorted(list(new_numbers), key= lambda x:-x[0])
        results = [M] * 1000
        for i in new_numbers:
            if min_cnt != 4:
                # path.append(i[0])
                find_min(i[0],i[1]+1)
                # path.pop()
    print(f'#{tc} {min_cnt}')


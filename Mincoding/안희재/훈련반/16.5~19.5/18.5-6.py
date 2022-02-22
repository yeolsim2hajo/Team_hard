win = [[3,5,1], [4,2,6]]
people = list(map(int,input().split()))

bucket = [0] * 10 # 0도 있으니까 * 10

for i in range(2):
    for j in range(3):
        index = win[i][j]
        bucket[index] = 1 # 중복없으니까 +=1 굳이 안해도~

for i in people:
    if bucket[i] == 1:
        print(f'{i}번 합격')
    else:
        print(f'{i}번 불합격')


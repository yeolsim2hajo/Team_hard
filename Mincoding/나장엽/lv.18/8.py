# 아파트 배열 선언
arr = [[15, 18, 17], [4, 6, 9], [10, 1, 3], [7, 8, 9], [15, 2, 6]]

input = list(map(int, input().split()))

# input에 해당하는 패턴이 arr에 있는지 찾는 문제.

# 밑에서부터 찾아야 하기 때문에 찾는 시도횟수가 층이라고 할 수 있음..
# 종료 조건을 주기위해 flag 선언. 찾으면 종료
# 두번의 반복문이기에 찾으면 종료시키기 위해 break가 2개필요~
# 

cnt = 0
for i in range(4, -1, -1): # 0 1 2 3 4 
    cnt += 1
    flag = 0
    for k in range(0, 3, 1):
        if input[k] == arr[i][k]:
            flag = 1
            break
    if flag == 1:
        break


print("{0}층".format(cnt))
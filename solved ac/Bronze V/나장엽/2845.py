from re import A


cnt_people, p =  list(map(int, input().split(' ')))
list_newspaper = list(map(int, input().split(' ')))

extent = cnt_people * p
result = 0

for i in range(0, len(list_newspaper)):
    result =  list_newspaper[i] - extent
    print(result, end=' ')


# 상도는 N개의 스위치와 M개의 램프를 가지고 있다.
# 스위치는 램프의 전원을 켤 수 있다.
# 스위치와 연결된 램프의 개수는 0개 이상이다. 0 <=
# 램프는 모두 꺼져있음
# 스위치를 이용해 램프의 전원을 킬 수 있지만, 전원을 끌 수느 ㄴ없다.
# 한 램프에 두 스위치가 연결되어 있는 경우에 한 스위치를 누르거나, 두 스위치를 모두 누르면 램프는 켜져 있는 상태가 된다
# n개의 스위치를 모두 누르면 모든 램프는 켜진다,
# 상도는 n-1개의 스위치를 눌러도 모든 램프가 켜지는지 궁금
# 스위칭와 램프의 연결 상태가 입력으로 주어진다.
# n-1개의 스위치를 눌러서 모든 램프를 켤 수 있는지 알아보자.\
# from collections import defaultdict

# n, m = map(int, input().split()) # 스위치의 수 n, 램프의 수 m
# data = dict()
# temp = []
# for i in range(n):
#     temp.append(list(map(int, input().split())))
#     connection = temp[i][1:]
#     data[i+1] += connection

# print(data)

from collections import defaultdict

def is_all_on(arr):
    on = False
    for i in range(1, len(arr)):
        if arr[i] == True:
            on = True
        else:
            on = False
            break
    return on


n, m = map(int, input().split()) # 스위치의 수 n, 램프의 수 m
switch = dict() # defaultdict로 선언
lamp = [False] * (m+1) # 스위치를 통해 램프가 켜졌는지 안 켜졌는지 체크하는 배열 일단 꺼둠

data = []
for i in range(n):
    data.append(list(map(int, input().split())))
    switch[i+1] = data[i][1:] # 스위치의 번호에, 연결된 램프를 할당한다 

cnt = 0
on = False # 램프가 다 켜져잇으면 true 아니면 false
for i in range(1, n+1): 
    for k in switch[i]: # 각 스위치의 values에 해당하는 값을 순회하면서, lamp의 인덱스와 비교하여 같으면 TRUE로 재할당
        lamp[k] = True # [false,true,false,false,false,false]
    cnt += 1 # 스위치 몇 번 눌렀는지 체크
    
    if cnt == n-1: # 만약 스위치를 누른 횟수가 n-1이고, 
        if is_all_on(lamp) == True: # 모든 램프가 다 켜져 있으면? 5개가 있을 때 이것이 다 true 
            print(1)
            break
        else:       
            print(0) 
            break
    

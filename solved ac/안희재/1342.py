# 행운의 문자열인지를 체크해주는 check함수는 따로 만들고,
# dfs로 같지 않은, 문자열 재배치 처리

def check(word):
    flag = True
    for k in range(len(word)-1):
        if word[k] == word[k+1]:
            flag = False
            break
    return flag

string = input()
arr = []
for i in range(len(string)):
    arr.append(string[i])

arr.sort()

cnt = 0
new_arr = []
visited = [0] * len(arr)

def dfs(level):
    if level == len(arr):
        if check(new_arr) == True:
            cnt += 1

    for k in range(len(arr)):
        
# ...난.. 쥬륵..

N,M = map(int,input().split())
arr = list(map(int,input().split()))
dir = [0]*(N+1)
dir[0] = -1 # 0번인덱스는 의미없

def group(a,b): # a를 보스로

    while(True):
        if dir[a] == 0: # 비어있으면(자신이 보스) 넘어가고
            # a = a ㅇㅇ.그대로.
            break
        else: # 비어있지 않다면, 
            a = dir[a] # 직속보스로 이동!(dir[a]값은 a의 보스가 적혀있음 / 0이면 자기가 보스고)

    while(True):
            if dir[b] == 0 or dir[b] == a:
                dir[b] = a
                break
            else:
                t = dir[b] # tmp
                dir[b] = a
                b = t

for i in range(M):
    a,b=arr[2*i],arr[2*i+1]
    if a > b:
        a,b = b,a
    group(a,b)

# print(dir)
print(dir.count(0))

# 5 3 
# 1 2 3 4 1 3 -> 인 경우,
# 내 코드는 0 "1 1 3 3 0" 되어서 마지막에 모든 3을 1로 덮어주는 코드가 필요했는데..
# 여기처럼 하면 어차피 그럴필요도 없구나..
# 0이라는 것은 그룹화가 아예 안되었거나 / 그룹의 주인이라는 뜻!!!!
# 0이 아니라는 것은? 어떤 그룹에 속해있다는 뜻
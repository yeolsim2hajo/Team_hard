train = [3,7,6,4,2,9,1,7]
team = list(map(int,input().split()))
# 연속

for i in range(7):
    if train[i:i+3] == team:
        print(f'{i}번~{i+2}번 칸')

# 슬라이딩 윈도우로도 가능 - 페어 코드
# def find(train,team):
#     G=[]
#     for i in range(len(team)):
#         G=G+[train[i]]
    
#     for j in range(len(train)-len(team)+1):
#         if G==team:
#             return j
#         if j== len(train)-len(team):
#             break
#         G=G[1:]+[train[j+len(team)]]
        
#     return '0'


# train=[3,7,6,4,2,9,1,7]
# team=list(map(int,input().split()))
# print(f'{find(train,team)}번~{find(train,team)+len(team)-1}번 칸')
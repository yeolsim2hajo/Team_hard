levelTable = [[10,20], [30,60], [100,150], [200,300]]
fruits = list(map(int,input().split()))

lev0 = 0
lev1 = 0
lev2 = 0
lev3 = 0

# 아 이거 도대체 어케 푸냐 ㅋㅋㅋㅋㅋ수업내용과 연계해서?? 이건 그냥 하드코딩임 ㅠㅠ
# lev0~3까지, 각 변수를 반복문하고 어떻게 연계해야 될지 모르겠음
# lev{i} 이렇게 할 수도 없고;;
for i in fruits:
    if i >= 10 and i <= 20:
        lev0 += 1
    elif i >= 30 and i <= 60:
        lev1 += 1
    elif i >= 100 and i <= 150:
        lev2 += 1
    elif i >= 200 and i <= 300:
        lev3 += 1        

print(f'lev0:{lev0}')
print(f'lev1:{lev1}')
print(f'lev2:{lev2}')
print(f'lev3:{lev3}')

# --------------------------------------
# 서준 코드
# def levelT(level,fruit):
#     count=0
#     for i in range(len(fruit)):
#         if level[0] <= fruit[i] <=level[-1]:
#             count +=1
#     return count
    
    
# levelTable=[[10,20],[30,60],[100,150],[200,300]]
# fruit=list(map(int,input().split()))

# for i in range(len(levelTable)):
#     print(f'lev{i}:{levelT(levelTable[i],fruit)}')
# 음.. 행을 y로, 열을 x로 표현한게 많네.. 민쌤도 그렇고..
    # 나도 스타일 바꿔야 하나..?
def move(Map, moving):
    x,y = 0,0
    for i,m in enumerate(Map):
        if 1 in m:
            x,y = m.index(1),i
    Map[y][x] = 0
    for i in moving:
        if i==1 and Map[y-1][x]!=2:
            y-=1
        elif i==2 and Map[y+1][x]!=2:
            y+=1
        elif i==3 and Map[y][x-1]!=2:
            x-=1
        elif i==4 and Map[y][x+1]!=2:
            x+=1
    Map[y][x] = 1
    for i in Map:
        print(i)
    return [x,y]
#88 지식이의 게임개발
# 지도의 크기, 장애물의 위치, 캐릭터의 위치 입력
'''
4 5
0 0
0 1
1 1
2 3
1 3
'''
def make_map(garo,sero,character,wall):
    result = [[2]*(garo+2)]
    result += [[2]+[0]*(garo)+[2] for _ in range(sero)]
    result.append([2]*(garo+2))
    for i in range(n):
        for j in range(n):
            if [i,j] == character:
                result[i+1][j+1] = 1
            elif [i,j] in wall:
                result[i+1][j+1] = 2
    return result

n, m = map(int,input().split()) # 가로, 세로
position = list(map(int,input().split()))
obstacles = [list(map(int,input().split())) for _ in range(4)]
make_map(n,m,position,obstacles)


#89 지식이의 게임개발2
# 4 5
# 0 0
# 0 1
# 1 1
# 2 3
# 1 3
# 2 2 2 4 4 4
# def move(info_map,info_motion):
#     dy=[0,-1,1,0,0]
#     dx=[0,0,0,-1,1]
#     y,x=position
#     y+=1
#     x+=1
#     while info_motion:
#         idx=info_motion.pop(0)
#         ny=y+dy[idx]
#         nx=x+dx[idx]
#         if 1<=ny<m+1 and 1<=nx<n+1 and info_map[ny][nx]!=2:
#             info_map[y][x] = 0
#             info_map[ny][nx] = 1
#             y,x=ny,nx
#     return info_map
#
# motion = list(map(int,input().split()))
# jido = make_map(n,m,position,obstacles)
# print('캐릭터 이동 전 지도')
# for i in range(m+2):
#     print(jido[i])
# print('\n캐릭터 이동 후 지도')
# for i in range(m+2):
#     print(move(jido,motion)[i])

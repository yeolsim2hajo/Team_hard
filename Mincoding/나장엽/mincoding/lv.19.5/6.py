map = [["A","B","G","K"],["T","T","A","B"],["A","C","C","D"]]

input = [list(input()) for _ in range(2)]

# 6번 반복해야 전체 map의 요소를 input과 검사할 수 있음
# 기준이 되는 좌표를 전달받는 함수를 만들고, 그것과 input를 비교해보자..
# 기준이 되는 좌표를 전달받으면...4번 검사해야함.. input은 고정되어잇어야함...4번 검사되는 동안.
# 기준점은 (0,0) (0,1) (0,2) (1,0) (1,1) (1,2)
# for y in range(2): for x in range(3) : find(y,x)


#함수를 만들어 보자
#2x2배열을 통해 전체를 검사해야함... input과 비교하기때문...!
#함수는 6번 호출되야함
#일치하지 않으면 return 0 을 반환해서 함수 종료 일치하면  return 1


def find(y, x):
    for i in range(2):
        for k in range(2):
            if map[y+i][x+k] != input[i][k]:
                return 0
    return 1 

cnt = 0
for y in range(2):
    for x in range(3):
        if find(y,x):
            cnt += 1

if cnt != 0:
    print("발견(%d개)"%cnt)
else:
    print("미발견")



# 원경님 코드
# arr = ['ABGK','TTAB','ACCD']
# map_arr = [list(map(str,arr[i])) for i in range(3)]
# pattern = [[x for x in input()] for _ in range(2)]

# dy = [0,1,0,1]
# dx = [0,0,1,1]
# cnt = 0
# for map_i in range(6):
#     for d_i in range(4):
#         if map_arr[map_i//3+dy[d_i]][map_i%3+dx[d_i]] != pattern[dy[d_i]][dx[d_i]]:
#             break
#     else: cnt += 1

# if cnt:
#     print(f'발견({cnt}개)')
# else:
#     print('미발견')
# 3X3 배열 선언
arr = [list(map(int, input().split())) for _ in range(3)]


# 1~9 까지 숫자 중 어떤 숫자들이 없는지를 찾아서 출력해라~
# dat를 사용하여 풀기. dat의 인덱스 값을 반환하면 될것 같은 느낌~?

# 인덱스 0 값은 어떻게 처리할까..?
# dat[0]을 삭제해버리면?
dat = [0]*10


for row in range(3):
    for col in range(3):
        dat[arr[row][col]] += 1


dat[0] = None
for i in range(len(dat)):
    if dat[i] == 0:
        print(i, end=' ')
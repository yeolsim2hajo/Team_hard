#lv9
#1 원하는 값을 찾아내자
arr = [4,3,6,1,3,1,5,3]
n = int(input())
cnt = 0
for element in arr:
    if n == element:
       cnt += 1
print('숫자%d개수는%d개'%(n,cnt))

#2 2차 배열에서 값찾기
arr = ['ABCDE','EABAB','ACDER']
munja = [list(map(str,arr[i])) for i in range(3)]
m = input()
cnt = 0
for i in range(3):
    cnt += munja[i].count(m)
if cnt >= 3:
    print('대발견')
elif cnt >= 1:
    print('발견')
else:print('미발견')

#3 둘 다 있어야해
arr = ['A','F','G','A','B','C']
mun, ja = input().split()
if mun in arr and ja in arr:
    print('와2개')
elif mun in arr or ja in arr:
    print('오1개')
else:print('우0개')

#4 숫자 교환하기
arr = [3,4,2,5,7,9]
a, b = map(int, input().split())
arr[a], arr[b] = arr[b], arr[a]
print(*arr)

#5 구조체 - 넘어감
#6 2차배열 값 SWAP 하기
arr = [[0]*3 for _ in range(3)]
for i in range(3):
    for j in range(3):
        arr[i][j] = chr(ord('A')+3*i+j)
y1,x1 = map(int, input().split())
y2,x2 = map(int, input().split())
arr[y1][x1],arr[y2][x2] = arr[y2][x2], arr[y1][x1]

for i in range(3):
    print(*arr[i],sep='')

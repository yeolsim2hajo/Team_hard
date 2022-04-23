# #lv14
# #1 while로 문제 풀기
# a, b = map(int, input().split())
# while a <= b:
#     print(a, end=' ')
#     a += 1
#
# # while말고
# print(*list(range(a, b+1)))
#
# #2 아파트 주민들
# arr = [list(map(int, input().split())) for _ in range(5)]
# for i in range(5):
#     people = 0
#     for j in range(4):
#         people += arr[i][j]
#     print(people, end=' ')
#
# #3 구조체 문제
# #4 구역 좁히기
# arr = input().split()
# for i in range(5):
#     for j in range(i,5):
#         print(arr[j], end=' ')
#     print()
#
# # 다른 방법
# for i in range(5):
#     print(*arr[i:])

#5 와플 발라먹기
arr = [list(map(int, input().split())) for _ in range(3)]

# arr = []
# for i in range(3):
#     arr += map(int, input().split())

jam = 0
# for i in range(3):
#     for j in range(3):
#         if i >= j:
#             jam += arr[i][j]
for i in range(3):
    for j in range(0,i+1):
        jam += arr[i][j]
print(jam)

for i in range(3):
    jam += sum(arr[i][:i+1])
print(jam)

#6 같은번호 개수 세기
vect = [3,5,1,1,2,3,2]
arr = list(map(int, input().split()))
# for i in range(4):
#     print(f'{arr[i]}={vect.count(i)}개')
#
# cnt = 0
# for i in range(4):
#     for j in range(7):
#         if arr[i] == vect[j]:
#             cnt += 1
#     print(f'{arr[i]}={cnt}개')

bucket = [0]*6
for i in range(7):
    bucket[vect[i]] += 1
for i in range(4):
    print(f'{arr[i]}={bucket[arr[i]]}개')

#7 선택정렬하기
arr = list(map(int, input().split()))
# arr.sort(reverse=True)
# print(*arr, sep='')

# print(*sorted(arr, reverse=True), sep='')

# print(*reversed(sorted(arr)),sep='')

for i in range(5):
    for j in range(i+1, 6):
        if arr[i] < arr[j]:
            arr[i], arr[j] = arr[j], arr[i]
print(*arr, sep='')

# 버블 정렬
for i in range(5):
    for j in range(5-i):
        if arr[j] < arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]
print(*arr, sep='')

#8 문장을 정렬해보자
arr = list(map(str,input()))

# DAT - arr이 list일 필요 없음
bucket = [0]*26
for i in range(len(arr)):
    idx = ord(arr[i]) - ord('A')
    bucket[idx] += 1
for i in range(26):
    if bucket[i]:
        print(chr(i+ord('A'))*bucket[i])

# 선택 정렬
for i in range(len(arr)-1):
    for j in range(i+1, len((arr))):
        if arr[i] > arr[j]:
            arr[i], arr[j] = arr[j], arr[i]
print(*arr, sep='')

# 버블 정렬
for i in range(len(arr)-1):
    for j in range(len(arr)-1-i):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]
print(*arr, sep='')

# 함수 사용
print(*sorted(arr),sep='')


#9 보다 큰 숫자 찾아내기
arr = [10,50,40,20,30,40]
arr_6 = list(map(int,input().split()))
# for i in range(6):
#     cnt = 0
#     for j in range(6):
#         if arr_6[i] < arr[j]:
#             cnt += 1
#     print(f'{arr_6[i]}={cnt}개')

# 이진 탐색 - 다시
arr.sort()
left = idx = cnt = 0
right = 5
while True:
    mid = (left+right)//2
    cnt += right-mid
    if arr_6[idx] == arr[mid] or right <= left:
        print(f'{arr_6[idx]}={cnt}개')
        idx += 1
        left = cnt = 0
        right = 5
    elif arr_6[idx] < arr[mid]:
        right = mid
    else:
        left = mid
        cnt = 0


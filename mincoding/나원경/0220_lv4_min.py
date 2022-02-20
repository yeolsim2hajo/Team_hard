#7 index값 입력받고 계산하기
arr = [3,9,27,81,243]
num = int(input())
print(arr[num]-100)

#8 응용문제 If와 For 같이 써보기
num = int(input())
if num > 5:
    for i in range(1,11):
        print(i)
else:
    for i in range(5,0,-1):
        print(i)

#9 배열값 거꾸로 출력
arr = [5,2,3,4,7]
for i in range(-1,-len(arr)-1,-1):
    print(arr[i], end=' ')

#10 배열의 2번 index값 출력하기
arr = [0]*6
num = int(input())
for i in range(6):
    arr[i] = num - i
print(arr[2])

#11 합구하기
arr = list(map(int, input().split()))
total = 0
for i in range(4):
    total += arr[i]
print(total)

#12 index값 입력받고 끝까지 출력
arr = [5,25,54,2,-33,57,82,-8,13,1]
idx = int(input())
for i in range(idx,len(arr)):
    print(arr[i])

#4.5

#1 index값 입력받고 출력하기
arr = list(map(int, '326718'))
num = int(input())
print(arr[num])

#2 복잡한 조건에 따라 문제 풀어보기
num = int(input())
if num != 3:
    print('3이 아니다')
if num != 5:
    print('5가 아니다')
if 1 < num < 10:
    for i in range(5, 0, -1):
        print(i)

#3 배열에 숫자를 순서대로 채우기
arr = [0]*5
num = int(input())
for i in range(5):
    arr[i] = num
for i in range(5):
    print(arr[i],end='')

#4 배열 하드코딩하기
arr = [1,7,3,2,6]
for i in range(5):
    print(arr[i],end='')

#5 1~3등까지만
arr = list(map(int, input().split()))
print(arr[0]+arr[1]+arr[2])

#6 첫번째칸 or 마지막칸
arr = [3,9,12,15,55]
num = list(map(int,input().split()))
total = 0
for i in range(3):
    total += num[i]
if total > 10:
    print(arr[-1])
else:
    print(arr[0])

#7 index값 입력받고 첫번째 까지 출력
arr = [5,7,1,8,-4,-73,4,2,20,84]
idx = int(input())
for i in range(idx,-1,-1):
    print(arr[i])

#8 순서대로 배열에 값 채우고 출력하기
num = int(input())
arr = list(range(num,num+6))
for i in range(6):
    print(arr[i])

#9 길건너 숫자
arr = [0]*4
n,m = map(int,input().split())
arr[0] = n
arr[2] = m
print(*arr,sep='')
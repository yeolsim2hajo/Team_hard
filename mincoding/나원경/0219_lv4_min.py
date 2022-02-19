#1 입력값을 배열에 넣고 그대로 출력하기
arr = input().split()
for i in range(len(arr)):
    print(arr[i],end=' ')

#2 인덱스의 값 출력
arr = [4,1,3,6,9]
number = int(input())
print(f'{number}번index의값은{arr[number]}입니다')

#3 처음과 끝
arr = list(map(int,input().split()))
print(arr[0]+arr[-1])

#4 플러스 알파
number = int(input())
arr = [number+5]*5
for i in range(5):
    print(arr[i],end=' ')

#5 a와 b의 합
arr = [3,4,1,6,7,5]
a,b = map(int,input().split())
print(arr[a]+arr[b])

#6 우와,유유
arr = [3,1,2,5]
n = int(input())
if arr[n] > 2:
    print('우와')
else:print('ㅠㅠ')
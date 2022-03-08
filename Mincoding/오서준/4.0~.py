
# #4-1. 입력값을 배열에 넣고 그대로 출력하기

# ar=list(map(int,input().split()))
# for i in ar:
#     print(i,end=' ')
    
# # 4-2. 인덱스의 값 출력
# ar=[4,1,3,6,9]
# i=int(input())
# print(f'{i}번index의값은{ar[i]}입니다')

# #4-4. 플러스 알파

# i=int(input())
# ar=[]
# for _ in range(5):
#     ar.append(i+5)
# print(*ar)

# # 4-5. a와 b의 합
# arr=[3,4,1,6,7,5]
# a,b=map(int,input().split())
# print(arr[a]+arr[b])

# # 4-6. 우와,유유
# ar=[3,1,2,5]
# index=int(input())
# if 2<ar[index]:
#     print('우와')
# else:
#     print('ㅠㅠ')

# # 4-7. index값 입력받고 계산하기
# ar=[3,9,27,81,243]
# index=int(input())
# print(ar[index]-100)

# # 4-8. 응용문제 If와 For 같이 써보기

# a= int(input())
# if 5<a:
#     for i in range(1,11):
#         print(i)
# else:
#     for i in range(5,0,-1):
#         print(i)

# # 4-9. 배열값 거꾸로 출력
# ar=[5,2,3,4,7]
# print(*ar[-1::-1])

# # 4-10. 배열의 2번 index값 출력하기

# ar=[0]*6
# a=int(input())
# for i in range(len(ar)):
#     ar[i]=a
#     a-=1
# print(ar[2])

# # 4-11. 합구하기
# ar=list(map(int,input().split()))
# sum=0
# for i in ar:
#     sum+=i
# print(sum)

# # 4-12. index값 입력받고 끝까지 출력
# ar=[5,25,54,2,-33,57,82,-8,13,1]
# index=int(input())
# for i in range(index,len(ar)):
#     print(ar[i])

# #4.5-1. index값 입력받고 출력하기
# ar=[3,2,6,7,1,8]
# i=int(input())
# print(ar[i])

# #4.5-2. 복잡한 조건에 따라 문제 풀어보기

# num=int(input())
# if num != 3:
#     print('3이 아니다')

# if num != 5:
#     print('5가 아니다')

# if 1<num<10:
#     for i in range(5,0,-1):
#         print(i)


# #4.5-3. 배열에 숫자를 순서대로 채우기
# ar=[0]*5
# num=int(input())
# for i in range(5):
#     ar[i]=num
# print(*ar,sep='')

# #4.5-4. 배열 하드코딩하기
# ar=[1,7,3,2,6]
# for i in ar:
#     print(i,end='')
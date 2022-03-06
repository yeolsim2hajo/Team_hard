
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
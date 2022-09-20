# DAT 이용해서 O(n)이 되도록! 해보기
T = int(input())

for k in range(1, T+1):
    str1 = list(input())
    str2 = list(input())
    bucket = [0] * 53
    
    for i in range(len(str2)):
        index = ord(str2[i])-65
        bucket[index] += 1

    max = 0
    for i in range(len(str1)):
        if bucket[ord(str1[i])-65] > max:
            max = bucket[ord(str1[i])-65]

    print(f'#{k} {max}')

# 실수1 : bucket 밖에다 꺼내놨었음..
# 실수2 : 소문자일수도 있잖아. 테스트케이스는 전부 대문자지만, 대문자만 입력받는다는 얘기 xx
# 실수3 : 또한, 버켓 크기는 넉넉잡게 잡는게 좋다.
# -> 따라서, 굳이 ord - 65할 필요가 없다. 아래 페어코드처럼 하면 됨
# 또한, 버켓크기 적게 작으면 교수님이 버그 걸린다고도 하셨음. 적당~히 크게 잡자

# - 페어코드 -> 실행시간, 코드 길이
# def Cnt(str1,str2):
#     arr=[0]*200
#     cnt=0
#     for i in range(len(str2)):
#         arr[ord(str2[i])]+=1
         
#     str1=set(str1)
#     str1=list(str1)
     
#     for i in range(len(str1)):
#         if arr[ord(str1[i])]> cnt:
#             cnt= arr[ord(str1[i])]
             
#     return cnt
 
# TC=int(input())
# for t in range(1,TC+1):
#     str1=input()
#     str2=input()
#     print(f'#{t} {Cnt(str1,str2)}')
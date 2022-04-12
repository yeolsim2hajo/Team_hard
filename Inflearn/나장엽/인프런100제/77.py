
#lcs 알고리즘
'''
Lcs의 가장 기초적인 문제
1. 두 문자열을 비교할때 사용할 리스트를 생성

서로 다른 두 문자열을 하나씩 비교하며 같다면 왼쪽 대각선 위쪽의 값+1
비교한 문자가 같지 않다면 왼쪽이나 오른쪽의 값 중 큰 값을 대입
두 문자열의 비교가 끝난 후 리스트의 가장 마지막 값 = 가장 긴 공통 부분 문자열

'''

arr1='ACAYKP' # y축 6
arr2='CAPCAK'# x축 7열

lst=[[0 for _ in range(len(arr2)+1)]for _ in range(len(arr1)+1)] # 6행    7열

for x in range(1,len(arr1)+1):
    for y in range(1,len(arr2)+1):
        if arr1[x-1] == arr2[y-1]:
            lst[x][y]=lst[x-1][y-1]+1
        else:
            lst[x][y]=max(lst[x-1][y],lst[x][y-1])

print(lst[-1][-1])
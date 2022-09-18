#n 입력받은 후
#arr배열에 n개의 정수 입력받기
#그리고 찾을 숫자(target)입력 받은 후
#bs를 이용하여 0(log(n))의 속도로 찾는 숫자가 있는 지 없는지 출력해 주세요

#! binary_search code
#* def binary_search(target, data):
#*     data.sort()
#*     start = 0
#*     end = len(data) - 1

#*     while start <= end:
#*         mid = (start+end) // 2
#*         if data[mid] == target:
#*             return mid
#*         elif data[mid] < target:
#*             start = mid + 1
#*         else:
#*             end = mid - 1


# 입력값
# 7
# 9 1 2 6 3 7 4
# 5
# 출력
# 없음.

n=int(input())
arr=list(map(int,input().split()))
target=int(input())

def bs(s,e,value):
    while(1):
        m=(s+e)//2
        if arr[m]==value:
            return 1
        elif arr[m]>value:
            e=m-1
        elif arr[m]<value:
            s=m+1
        if s>e:
            return 0
        
arr.sort()
answer=bs(0,n-1,target)
if answer:
    print("찾음")
else:
    print("없음")

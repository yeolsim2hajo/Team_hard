arr = ["A", "T", "K", "P", "T", "C", "A", "B", "C"]
str1, str2 = list(input().split())

# str1 은 왼쪽부터 오른쪽으로 검사
# str2 는 오른쪽부터 왼쪽으로 검사
# 검색해서 가장 먼저 발견되는 글자가 얼마나 떨어져 있는가? = 검색횟수를 저장하는 변수 선언해서 풀자.
# str1의 인덱스와 str2의 인덱스를 빼면 거리를 구할 수 있을 듯




# str1 검색
index1 = 0
for i in range(0, len(arr)):
    if str1 == arr[i]:
        index1 = i
        break

#str2 검색
index2 = 0
for k in range(len(arr)-1, -1, -1):
    if str2 == arr[k]:
        index2 = k
        break

print(abs(index2 - index1))
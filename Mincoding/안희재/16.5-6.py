# ord쓰면 금방 풀리는데 음.....................
# 다른 방법 없나? 오늘 배운거하고 동떨어진 풀이 같음
str_lst = list(input())

def maxindex(lst):
    max = ord(lst[0])
    for i in range(1,len(lst)):
        if max < ord(lst[i]):
            max = ord(lst[i])
    for i in range(len(lst)):
        if ord(lst[i]) == max:
            return i

def minindex(lst):
    min = ord(lst[0])
    for j in range(1,len(lst)):
        if min > ord(lst[j]):
            min = ord(lst[j])
    for j in range(len(lst)):
        if ord(lst[j]) == min:
            return j

print(maxindex(str_lst))
print(minindex(str_lst))
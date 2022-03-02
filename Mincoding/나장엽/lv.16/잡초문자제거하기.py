arr = [""]*7
str = list(input())
index = int(input())


# 입력받은 문자열을 arr 리스트에 저장.
for i in range(0, len(str)):
    arr[i] = str[i]


arr[index] = ''


for idx in range(index, len(str)-1, 1):
    arr[idx] = arr[idx+1]

arr[-1]=''

for k in arr:
    print(k, end='')

#! 원경님 풀이. bubble sort

# word = list(map(str,input()))
# index = int(input())

# for i in range(index,len(word)-1):
#     word[i], word[i+1] = word[i+1], word[i]

# for j in range(len(word)-1):
#     print(word[j], end='')
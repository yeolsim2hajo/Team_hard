# str1 = list(input())
# str2 = list(input())
# str3 = list(input())




# # ord 함수 쓰기.. #알파벳의 아스키 코드는 대문자 65 ~ 90  소문자 97 ~ 122 dat의 크기는 123으로 설정
# dat = [0]*123

# for i in range(len(str1)):
#     dat[ord(str1[i])] += 1

# for k in range(len(str2)):
#     dat[ord(str2[k])] += 1

# for j in range(len(str3)):
#     dat[ord(str3[j])] += 1

# result = 0

# for idx in range(len(dat)):
#     if dat[idx] >=2:
#         result = 1


# if result == 1:
#     print("No")
# else:
#     print("Perfect")

# 다른 풀이
# 문장의 길이를 구해서 그만큼 반복해서 DAT에 1을 누적시키면 되려나?
arr = [list(input()) for _ in range(3)]

# 문장의 길이 구하기...
# 문장의 길이를 저장할 변수 length를 선언하고, 그 안에 입력받은 문장의 길이를 저장하기.

length = []
for i in range(3):
    length.append(len(arr[i]))

# 문장의 길이만큼 dat에 1을 누적시키는 것을 반복하기
# 한방에 안되나......?
dat = [0]*123

# 입력받은 문장의 길이만큼 반복시키고 dat에 1을 누적시키기
for k in range(3):
    for j in range(0, length[k]):
        dat[ord(arr[k][j])] += 1

# 반복되는 알파벳이 있다면 dat의 값이 2 이상 됨... 따라서 2 이상이면 result에 1을 넣어서 반복된 알파벳이 있다고 판단
result = 0
for idx in range(len(dat)):
    if dat[idx] >=2:
        result = 1

if result == 1:
    print("No")
else:
    print("Perfect")
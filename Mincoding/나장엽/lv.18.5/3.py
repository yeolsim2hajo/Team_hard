# 한 문장을 입력받고,
# 가장 많은 알파벳이 어떤 알파벳인지 출력해라..

# dat ord chr 사용해서 풀기


arr = list(input())

#알파벳의 아스키 코드는 대문자 65 ~ 90  소문자 97 ~ 122 
dat = [0]*123

for i in range(len(arr)):
    dat[ord(arr[i])] += 1

result = 0
max = dat[0]
for k in range(len(dat)):
    if max < dat[k]:
        max = dat[k]
        result = k
    else:
        max = max


print(chr(result))


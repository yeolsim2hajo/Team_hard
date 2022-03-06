arr = list(input())
# 아스키 코드로 풀어봅시다
# A는 65 Z는 65+26=91
dat = [0] * 92

# dat 리스트에 1씩 체크. 많으면 점점 1씩 늘어나는 코드
for k in range(len(arr)):
    dat[ord(arr[k])] += 1

# dat에 누적합으로 가장 많이 나온 알파벳을 구했으므로, max를 이용하여 풀자
# max값 초기화
max = dat[0]
index = 0
for i in range(len(dat)):
    if max < dat[i]:
        max = dat[i]
        index = i
    else:
        max = max

print(chr(index))
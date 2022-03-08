# 뭐야 ord쓰는건가? 
# ord('A') = 65
# 아니면, alphabet = ['A', 'B', ...'Z'] 하드코딩해놓고 인덱스 지정해두면 되긴 하는데 그렇게까진 아닐듯
a = input()
bucket = [0] * 27

for i in range(len(a)):
    index = ord(a[i])-65  # 이러면 'A'는 0번인덱스에 담기지
    bucket[index] += 1

max = 0
max_index = 0
for i in range(len(bucket)):
    if bucket[i] > max:
        max = bucket[i]
        max_index = i

print(chr(max_index+65))
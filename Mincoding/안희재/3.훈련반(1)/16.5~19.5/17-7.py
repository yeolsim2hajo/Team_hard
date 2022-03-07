bucket = [[0,0,1,0,0], [0,0,1,1,1]]
arr = [[3,5,4,1,1], [3,5,2,5,6]]

mask_arr = []

for i in range(2):
    for j in range(5):
        if bucket[i][j] == 1:
            mask_arr.append(arr[i][j])

num = int(input())

for k in mask_arr:
    result = f'{num} 없음'
    if num == k:
        result = f'{num} 존재'
        break
    else:
        continue

print(result)
# 아 ㅅㅂ 드디어 내 방식으로 풀었다 - continue를 break하고 같이 쓰면 되는구나
# 변수 하나에 디폴트값 설정해두고
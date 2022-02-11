# 10179

# 10701 수도요금 - 다시

from calendar import month


a = int(input())
b = int(input())
c = int(input())
d = int(input())
p = int(input())

x = a * p
y = b * p

if c < p:
    y += (p - c) * d

print(min(x, y))


# 10768 특별한 날
m = int(input())
d = int(input())
if m < 2:
    print('Before')
elif m == 2 and d < 18:
    print('Before')
elif m == 2 and d == 18:
    print('Special')
else:
    print('After')

# 10797 10부제
day = input()
arr = input().split()
cnt = 0
for element in arr:
    if element[-1] == day:
        cnt += 1
print(cnt)

# 11282 한글
n = int(input())
print(chr(n + ord('가') - 1))

# 11943 파일 옮기기
bas = list(map(int, input().split()))
ket = list(map(int, input().split()))
if bas[0] + ket[1] > bas[1] + ket[0]:
    print(bas[1] + ket[0])
else:
    print(bas[0] + ket[1])

# 11948 과목 선택
arr = [0]*6
for i in range(6):
    arr[i] = int(input())
print(sum(arr) - min(arr[:4]) - min(arr[4:]))

# 13136 Do Not Touch Anything
r, c, n = map(int, input().split())
r_n = r//n
c_n = c//n
if r % n:
    r_n += 1
if c % n:
    c_n += 1
print(r_n * c_n)

# 13866 팀 나누기 - 나중에
arr = list(map(int, input().split()))
min_dif = max(arr)

for i in range(len(arr)):
    for j in range(i+1, len(arr)):
        if sum(arr) - (arr[i] + arr[j]) < min_dif :
            min_dif = sum(arr) - (arr[i] + arr[j])
print(min_dif)
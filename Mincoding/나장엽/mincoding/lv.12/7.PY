from re import A


arr = list(input())
a = input()
b = input()
c = input()
cnt1 = 0
cnt2 = 0
cnt3 = 0
for i in range(len(arr)):
    if arr[i] == a:
        cnt1 += 1
    if arr[i] == b:
        cnt2 += 1
    if arr[i] == c:
        cnt3 += 1

print(f'{a}={cnt1}')
print(f'{b}={cnt2}')
print(f'{c}={cnt3}')
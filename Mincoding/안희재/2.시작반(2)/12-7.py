word = input()
a = input()
b = input()
c = input()

cnt_a = 0
for ele in word:
    if ele == a:
        cnt_a += 1
print(f'{a}={cnt_a}')

cnt_b = 0
for ele in word:
    if ele == b:
        cnt_b += 1
print(f'{b}={cnt_b}')

cnt_c = 0
for ele in word:
    if ele == c:
        cnt_c += 1
print(f'{c}={cnt_c}')
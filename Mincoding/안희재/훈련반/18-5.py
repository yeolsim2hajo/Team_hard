# 뭐지 이거 bucket을 2개 만들어야 하나?
# DAT로 풀려면 흠;;
town = [['C','D','A'], ['B','M','Z'], ['Q','P','O']]
blacklist = input()
bucket = [0] * 27

for i in range(3):
    for j in range(3):
        index = ord(town[i][j])-65
        bucket[index] = 1 # 사람이니까, 중복은 없는 셈. 출입기록(횟수)도 아니니까

cnt = 0
for i in blacklist:
    if bucket[ord(i)-65] == 1:
        cnt += 1

print(f'{cnt}명')
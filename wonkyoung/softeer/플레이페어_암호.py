#230319
target = input() # 암호화할 문자열
key = input() # 암호키
match = {chr(i+65):-1 for i in range(26)} # 위치
del match['J'] # 'J' 삭제
table = [[''] * 5 for _ in range(5)] # 표
num = 0

for iterable in (key, match):
    for alp in iterable:
        if match[alp] == -1:
            quot, remain = divmod(num, 5)
            table[quot][remain] = alp
            match[alp] = (quot, remain)
            num += 1

i = 0
length = len(target)
result = ''
def add_alp():
    global result
    if row1 == row2:
        for col in (col1, col2):
            if col < 4:
                result += table[row1][col+1]
            else:
                result += table[row1][0]
    elif col1 == col2:
        for row in (row1, row2):
            if row < 4:
                result += table[row+1][col1]
            else:
                result += table[0][col1]
    else:
        for row, col in (row1, col2), (row2, col1):
            result += table[row][col]

while i < length - 1:
    alp = target[i]
    next_alp = target[i+1]
    row1, col1 = match[alp]
    if alp == next_alp:
        row2, col2 = match['X' if alp != 'X' else 'Q']
        i += 1
    else:
        row2, col2 = match[next_alp]
        i += 2
    add_alp()
if i == length - 1:
    alp = target[i]
    row1, col1 = match[alp]
    row2, col2 = match['X']
    add_alp()
print(result)
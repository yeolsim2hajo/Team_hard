#221224
words = []
length = []
for _ in range(5):
    words.append(input())
    length.append(len(words[-1]))
answer = ''
for j in range(max(length)):
    for i in range(5):
        if length[i] > j:
            answer += words[i][j]
print(answer)


# 함수
def read_vertical():
    words, length = [], []
    for _ in range(5):
        words.append(input())
        length.append(len(words[-1]))
    answer = ''
    for j in range(max(length)):
        for i in range(5):
            if length[i] > j:
                answer += words[i][j]
    return answer

print(read_vertical())


# try - except
def read_vertical():
    words, length = [], []
    for _ in range(5):
        words.append(input())
        length.append(len(words[-1]))
    answer = ''
    for j in range(max(length)):
        for i in range(5):
            try:
                answer += words[i][j]
            except Exception:
                pass
    return answer

print(read_vertical())
import sys
sys.stdin = open("input.txt", 'r')

def set_cipher_text():
    idx = 0
    for j in range(C):
        for i in range(R):
            cipher_text[i][j] = s[idx]
            idx += 1

def get_dkey():
    sorted_key = sorted(key)
    visited = [False]*C
    dkey = [0]*C
    for i in range(C):
        for j in range(C):
            if sorted_key[j] == key[i] and not visited[j]:
                visited[j] = True
                dkey[j] = i
                break
    return dkey

def get_plain_text():
    plain_text = [['' for _ in range(C)] for _ in range(R)]
    for i in range(R):
        for j in range(C):
            plain_text[i][d_key[j]] = cipher_text[i][j]
    return plain_text

def print_plain_text():
    print(*map(lambda x: ''.join(x), plain_text), sep='')

key = list(input())
s = input()
C = len(key)
R = len(s)//C
cipher_text = [['' for _ in range(C)] for _ in range(R)]
set_cipher_text()

d_key = get_dkey()
plain_text = get_plain_text()
print_plain_text()
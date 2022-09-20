import sys
input = sys.stdin.readline

N = int(input())
password =  dict()

for _ in range(N) :
    word = input().rstrip()
    rev_word = word[::-1]
    if word in password :
        password[word] += 1
    elif rev_word in password :
        password[rev_word] += 1
    else :
        password[word] = 1

result = sorted(password.items(), key= lambda x: -x[1])
word = result[0][0]
middle = word[len(word)//2]
answer = str(len(word)) + " " +  str(middle)
print(answer)
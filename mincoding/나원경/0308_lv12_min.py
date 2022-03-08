# lv.11

#1 문장 입력받고 출력하기
word = input()
for _ in range(5):
    print(word)

#2 두 문장의 길이는?
mun = input()
ja = input()
print(len(mun), len(ja))

#3 네 줄 카운트다운
n = int(input())
for i in range(4):
    for _ in range(4):
        print(n-i,end='')
    print()

#4 one two three 빌딩
n = int(input())
for _ in range(n):
    for i in range(1,4):
        print(i,end='')
    print()

#5 중첩 for문 활용하기
n = int(input())
for i in range(3):
    for j in range(4):
        if i + j > 1:
            print(n,end='')
            n += 1
        else:
            print(' ',end='')
    print()
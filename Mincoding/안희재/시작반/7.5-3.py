word = input().split()

if word[0].isupper() and word[1].isupper():
    print('대문자들')
elif word[0].isupper() == 0 and word[1].isupper() == 0:
    for i in range(26):
        print(chr(i+97),end='')
else:
    print('대소문자')
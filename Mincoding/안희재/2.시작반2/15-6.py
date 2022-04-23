word = input()

result = '개구리문장'
for i in range(len(word)):
    if i % 2 == 0 and word[i].isupper() == 0:
        result = '일반문장'
        print(result)
        break
    if i % 2 == 1 and word[i].islower() == 0:
        result = '일반문장'
        print(result)
        break
else:
    print(result)

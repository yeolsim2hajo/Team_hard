word = input().split()

standard = ord(word[0])
result = f'옳다{word[0]}'
for i in range(1,len(word)):
    if standard < ord(word[i]):
        result = '옳지않음'

print(result)
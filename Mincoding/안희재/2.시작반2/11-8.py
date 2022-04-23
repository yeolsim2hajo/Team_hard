arr = ['S','t','r','u','c','t','P','o','i','n','t','e','r']
word = input()

result = '미발견'
for i in arr:
    if i == word:
        result = '발견'
        break

print(result)

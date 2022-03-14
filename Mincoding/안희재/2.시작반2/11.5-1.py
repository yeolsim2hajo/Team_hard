arr = ['D','F','G','D','A','Q']

word = input().split()

for ele in arr:
    if ord(word[0]) <= ord(ele) <= ord(word[1]):
        print('발견!!!')
        break
else:
    print('미발견!!!')

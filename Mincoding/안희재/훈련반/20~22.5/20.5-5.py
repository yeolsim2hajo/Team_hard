word = input()
# 'A': 65, 'Z': 90

word_num = ord(word)
bucket = [word_num-3,word_num-2,word_num-1,word_num,word_num+1,word_num+2,word_num+3]
for i in range(7):
        if bucket[i] > 90:
                bucket[i] -= 26
        elif bucket[i] < 65:
                bucket[i] += 26
        print(chr(bucket[i]), end='')

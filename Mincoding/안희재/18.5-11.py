str = list(input())

bucket = [0] * 26

for i in range(len(str)):
    index = ord(str[i]) - 65
    bucket[index] = 1

if bucket[6] == bucket[7] == bucket[14] == bucket[18] == bucket[19] == 1:
    print('존재')
else:
    print('존재하지 않음')

# a b c d e f g h i j k l m n o p q r s t u 
# 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9
# 6 7 14 18 19
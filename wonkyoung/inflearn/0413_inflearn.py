import csv
# https://subinium.github.io/kaggle-basic/python/csv
# beginner
# input_file = open('sample_input (5).txt','r',encoding='utf-8')
# reader = csv.reader(input_file)
# for line in reader:
#     print(line)
# input_file.close()
#
# output_file = open('result.txt','w',encoding='utf-8')
# writer = csv.writer(output_file)
# writer.writerow([1,'Alice',True])
# output_file.close()
#
# #intermediate
# with open('sample_input (5).txt') as csv_file:
#     reader = csv.DictReader(csv_file)
#     for i in reader:
#         print(i)
#
# # Advanced : pandas
# import numpy as pd
# train = pd.read_csv('./train.csv')
# text = pd.read_csv('./test.csv')
# train.describe(include='all')

import csv
def sol(d):
    numbers = ['0','1','2','5','7','8','9']
    def bfs():
        nonlocal num1, num2
        from collections import deque
        q = deque()
        q.extend([i for i in numbers if i != '0'])
        while q:
            result = q.popleft()
            str_num = str(number - int(result))
            for element in str_num:
                if element not in numbers:
                    break
            else:
                num1 = result
                num2 = str_num
                return
            for i in range(6):
                result += numbers[i]
                q.append(result)

    output_file = open('result.txt','w',encoding='utf-8')
    writer = csv.writer(output_file)
    for line in d:
        money = list(map(str,line[1]))
        # print(money)
        idx = 0
        for i in range(len(money)-1,0,-1):
            if money[i] =='0':
                if idx == 0:
                    idx = i
            elif money[i] == ',':
                money.pop(i)
        number = int(''.join(money[:idx+1]))
        num1 = num2= ''
        bfs()
        length = len(money)
        money.pop(1)
        num1 += '0'*(length-idx-1)
        num2 += '0'*(length-idx-1)
        j = length-1
        cnt = 1
        while j > 0:
            if cnt==3:
                num1 = num1[:j]+','+num1[j:]
                num2 = num2[:j]+','+num2[j:]
                cnt = 0
                j -= 1
            cnt += 1
            j -= 1
        line.pop(1)
        line.insert(1,num1)
        line.insert(1,num2)
        line[0] = line[0].strip(',')
        writer.writerow(line)
    output_file.close()

input_file = open('test_inf.txt','r',encoding='utf-8')
data = csv.reader(input_file, delimiter=' ')
sol(data)
input_file.close()





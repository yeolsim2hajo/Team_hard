# 내보내기
#
# import csv
# # https://subinium.github.io/kaggle-basic/python/csv
# # beginner
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



# 입력값 생성
import random
random.sample(range(0,101), 1)

#
#
# l = [chr(i) for i in range(65,91)]
# total_medicine = []
# medicine = []
# check = {}
# for i in range(26):
#     check[l[i]] = 0
#
# for i in range(8):
#     medicine.append(r.choice(l))
#     check[medicine[i]] = True
#
# similar = 0
# for i in range(10):
#     total_medicine.append(r.sample(l,8))
#     cnt = 0
#     for j in range(8):
#         key = total_medicine[i][j]
#         if check[key]:
#             cnt += 1
#         if cnt > 4:
#             break
#     if cnt == 4:
#         similar += 1
#
# print(similar)

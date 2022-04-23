#90 같은 의약 성분을 찾아라
# import random as r
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


#92 키보드 고장 - 다시
# import csv
# def sol(d):
#     number = int(d[1])
#     half = str(number//2)
#     for num in half:
#         if num in {3, 4 ,6}:
#             break
#     else:
#         d[1] = half
#         d.insert(1,half)
#         return
#
#
#
#
# with open('sample_input (5).txt',newline='', encoding='utf-8') as f:
#     reader = csv.reader(f)
#     for row in reader:
#         data = row[0].split()
#         sol(data)
#         with open('result.txt','w',newline='') as csv_file:
#         csv_writer = csv.writer(csv_file)
#         csv_writer.writerow(data)

#94
#96
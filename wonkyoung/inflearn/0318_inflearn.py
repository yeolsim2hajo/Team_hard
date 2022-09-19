#57 내장함수 응용
# cnt = 0
# for i in range(1000):
#     cnt += str(i).count('1')
# print(cnt)

#58 콤마 찍기
# n = input()
# m = ''
# for i in range(len(n)-1):
#     m += n[i]
#     if i % 3 == 2:
#         m += ','
# m += n[-1]
# print(m)

#59 빈칸채우기
# munja = input()
# length = (50-len(munja))//2
# print('='*length+munja+'='*length)


#60 enumerate
# student = ['강은지','김유정','박현서','최성훈','홍유진','박지호','권윤일','김채리','한지호','김진이','김민호','강채연']
# insert_sort = []
# for i in range(len(student)):
#     insert_sort.append(student[i])
#     for j in range(i,0,-1):
#         if insert_sort[j] < insert_sort[j-1]:
#             insert_sort[j], insert_sort[j-1] = insert_sort[j-1], insert_sort[j]
# for i in range(len(student)):
#     print('번호: {}, 이름: {}'.format(i+1,insert_sort[i]))

# # enumerate, sort() 사용
# student.sort()
# idxn = list(enumerate(student,start=1))
# for i in range(len(student)):
#     print('번호: %d, 이름: %s' % (idxn[i][0],idxn[i][1]))


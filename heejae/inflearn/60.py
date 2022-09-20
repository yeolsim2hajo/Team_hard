student = ['강은지','김유정','박현서','최성훈','홍유진','박지호','권윤일','김채리','한지호','김진이','김민호','강채연']
student.sort()

answer = list(enumerate(student))
for i in range(len(answer)):
    print(f'번호: {answer[i][0]}, 이름: {answer[i][1]}')

# for number, name in enumerate(students):
#     print("번호: {}, 이름: {}".format(number+1, name))
# 아 그냥 이렇게 하면 되는구나..
# 반복문 안에서 enumerate만들고, 바로 출력시키기!!
# 내 코드와 한줄 차이지만, 작업량 자체는 2배일듯..
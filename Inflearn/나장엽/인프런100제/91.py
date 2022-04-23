import random as r
#내가 왜 입력데이터를 만들어야되는데??
#개똥같은 문제같으니라고

total_score = []
class_score = []
student_score = []

for i in range(7):
    class_score = []
    for i in range(30):
        student_score = []
        for i in range(5):
            student_score.append(r.randint(40, 100))
        class_score.append(student_score)
    total_score.append(class_score)

total_average = 0
class_average = []
student_average = 0

for Class in total_score:
    for Student in Class:
        student_average += sum(Student)//5
    class_average.append(student_average//30)
    student_average = 0 # 값 초기화

print(class_average)
print(sum(class_average)//len(class_average))
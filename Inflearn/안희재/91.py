import random as r

total = []
classs = []
student = []

for i in range(7):
    classs = []
    for i in range(30):
        student = []
        for i in range(5):
            student.append(r.randint(40, 100))
        classs.append(student)
    total.append(classs)
    
total_average = 0
c_average = []
s_average = 0

for c in total:
    for s in c:
        s_average += sum(s)/5
    c_average.append(s_average // 30)
    s_average = 0

print(c_average)
print(sum(c_average)//len(c_average))
# codeFestival_1. 91번

import random as r

score = []
class_score = []
student_score = []

ans = 0
for i in range(7):
    class_score = []
    a = 0
    b = 0
    for j in range(30):
        student_score = []
        for k in range(5):
            student_score.append(r.randint(1, 100))
        a += sum(student_score)
        if b < sum(student_score):
            b = sum(student_score)
        class_score.append(student_score)
    # 2.
    print(a/150)
    # 3.
    print(b/5)
    score.append(class_score)
    ans += a
# 1.
print(score)
# 4.
print(ans/1050)
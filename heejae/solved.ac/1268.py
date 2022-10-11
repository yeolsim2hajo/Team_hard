N = int(input())
students = []
for i in range(N):
    students.append([int(j) for j in input().split()])
# print(students)

max_friend = -1
banjang = -1
for student_no in range(N):
    result =set()
    for grade in range(5):
        for friend in range(N):
            if students[student_no][grade] == students[friend][grade]:
                result.add(friend)               
    
    if len(result) > max_friend:
        banjang = student_no +1
        max_friend = len(result)
        

print(banjang)
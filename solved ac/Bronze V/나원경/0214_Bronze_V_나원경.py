# 1550 16진수 - 틀렸는데 왜 틀린지 모르겠음

number = input()
new_num = 0
for i in range(len(number)):
    for j in range(6):
        if number[i] == chr(ord('A')+j):
            new_num += 10+j
            break
    else:
        new_num += int(number[i])
print(new_num)

# 10699 - 틀림

from datetime import datetime

print(f'{datetime.now().year - 7}-0{datetime.now().month - 1}-{datetime.now().day + 10}')



# 16170 - 
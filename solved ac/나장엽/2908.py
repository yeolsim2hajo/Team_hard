
number1, number2 = input().split() # '734', '893'
temp1, temp2 = [], []

for i in range(len(number1)-1, -1, -1):
    temp1.append(number1[i])
    temp2.append(number2[i])

number1 = ''.join(temp1)
number2 = ''.join(temp2)

number1 = int(number1)
number2 = int(number2)

if  number1 < number2 :
    print(number2)
else:
    print(number1)
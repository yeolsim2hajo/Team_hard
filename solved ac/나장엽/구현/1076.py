# 섹은 저항의 값
# 마지막 색은 곱해야 하는 값.
# 저항의 값은 다음 표를 이용해서 구한다

resist = {
    'black' : '0',
    'brown' : '1', 
    'red' : '2',
    'orange' : '3',
    'yellow' : '4',
    'green' : '5',
    'blue' : '6',
    'violet' : '7',
    'grey' : '8',
    'white' : '9'
}
multiply = [10**i for i in range(0, 10)]

data = []
for _ in range(3):
    data.append(resist[input()])

first = data[0] # 4
second = data[1] # 7
third = data[2] # 

temp = first + second
answer = int(temp) * multiply[int(third)]
print(answer)
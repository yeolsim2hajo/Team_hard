# 분수 찾기
input_num = int(input())

line = 0  # 사선 라인
max_num = 0  # 입력된 숫자(input_num 변수)의 라인에서 가장 큰 숫자
while input_num > max_num:
    line += 1  
    max_num += line  

gap = max_num - input_num 
if line % 2 == 0:  # 사선 라인이 짝수번째 일 때
    top = line - gap  #분자
    under = gap + 1  #분모
else :  # 사선 라인이 홀수번째 일 때
    top = gap + 1  #분자
    under = line - gap  #분모
print(f'{top}/{under}')
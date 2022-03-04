# 문자 입력받고 아스키코드 값 기준 -3 ~ 3 까지 출력해라

arr = input()


# 반복횟수라... -3 ~ 4 + 1 / -3 -2 -1 0 1 2 3
# 기준이 되는 것이 0이라 치면... ord(n) =


for i in range(-3, 4, 1):
    str = chr(((ord(arr)-ord('A')+i)%26)+ord('A'))
    print(str, end=' ')
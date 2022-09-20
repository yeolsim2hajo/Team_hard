word = input()
print("{0:=^10}".format(word))

# 처음엔, length구해서, 좌측/우측을 (50-length) //2로 했지만,
# format함수 사용하는게 더 편하다
# https://sinaworld.co.kr/30
# > 오른쪽정렬, < 왼쪽정렬, ^가운데정렬
# 위처럼 >, <, ^왼쪽에 문자 쓰면 그 문자를 나머지 자리에 채움
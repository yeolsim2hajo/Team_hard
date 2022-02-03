# 함수 내부에 불필요한 print문이 있는 경우 오답으로 처리가 됩니다.
def dec_to_bin(n):
    # 십진수를 이진수로 변환해 문자열로 반환 - 나머지를 거꾸로 출력
    # 재귀를 이용해 구현

    if n > 1: # 재귀 종료 조건 설정
        return str(dec_to_bin(n // 2)) + str(n % 2)
    else: # n이 0이나 1일 경우
        return n


# 아래의 코드를 수정하거나 새롭게 추가하지 않습니다.
if __name__ == '__main__':
    print(dec_to_bin(10))
    # 1010
    print(dec_to_bin(5))
    # 101
    print(dec_to_bin(50))
    # 110010
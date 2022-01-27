# 함수 내부에 불필요한 print문이 있는 경우 오답으로 처리가 됩니다.
def caesar(word, n):
    
    # 문장의 각 알파벳 양의 정수 n만큼 밀어 다른 알파벳으로 바꾸기
    # 소문자는 소문자로, 대문자는 대문자로 암호화
    new_word = ''
    new_string = ''

    for string in word:
        if 65 <= ord(string) <= 90:
            if ord(string) + n > 90:
                new_string = ord(string) + n - 26
            else:
                new_string = ord(string) + n
        else:
            if ord(string) + n > 122:
                new_string = ord(string) + n - 26
            else:
                new_string = ord(string) + n
        new_word += chr(new_string)

    return new_word


# 아래의 코드를 수정하거나 새롭게 추가하지 않습니다.
if __name__ == '__main__':
    print(caesar('apple', 5))
    # fuuqj
    print(caesar('ssafy', 1))
    # ttbgz
    print(caesar('Python', 10))
    # Zidryx
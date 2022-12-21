#221221
word = input()
answer = 1 if word == word[::-1] else 0
print(answer)

# 함수
def is_palindrome():
    word = input()
    answer = 1 if word == word[::-1] else 0
    return answer
print(is_palindrome())

# 인자
def is_palindrome(word):
    answer = 1 if word == word[::-1] else 0
    return answer
word = input()
print(is_palindrome(word))


# 변수 X
def is_palindrome(word):
    return 1 if word == word[::-1] else 0
word = input()
print(is_palindrome(word))

# 변수 X
def is_palindrome():
    word = input()
    return 1 if word == word[::-1] else 0
print(is_palindrome())

# int
def is_palindrome():
    word = input()
    return int(word == word[::-1])
print(is_palindrome())


# for
def is_palindrome():
    word = input()
    for i in range(len(word)):
        if word[i] != word[-1-i]:
            return 0
    return 1
print(is_palindrome())


# 변수
def is_palindrome():
    word = input()
    length = len(word)
    for i in range(length):
        if word[i] != word[-1-i]:
            return 0
    return 1
print(is_palindrome())
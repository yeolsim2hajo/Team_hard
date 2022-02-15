arr = ['M','T','K','C']

a = input()

def isExist(str):
    for i in arr:
        if str == i:
            return "발견"
    else:
        return "미발견"
    # els부분 for문 안쪽에 썻네 ㅅㅂ...;;;break처럼 써야함..
print(isExist(a))
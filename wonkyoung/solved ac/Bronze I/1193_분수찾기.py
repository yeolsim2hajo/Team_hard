#221221
X = int(input())
n = 1
total = (n * (n+1))//2
while True:
    dif = total - X
    if dif >= 0:
        if n%2 == 0:
            answer = f'{n-dif}/{1+dif}'
        else:
            answer = f'{1+dif}/{n-dif}'
        break
    n += 1
    total = (n * (n+1))//2
print(answer)


# 함수 - 시간 더 걸림
def find_nst():
    X = int(input())
    n = total = 1
    while True:
        dif = total - X
        if dif >= 0:
            if n%2 == 0:
                answer = f'{n-dif}/{1+dif}'
            else:
                answer = f'{1+dif}/{n-dif}'
            break
        n += 1
        total = (n * (n+1))//2
    return answer
print(find_nst())

# break 대신 return
def find_nst():
    X = int(input())
    n = total = 1
    while True:
        dif = total - X
        if dif >= 0:
            if n%2 == 0:
                return f'{n-dif}/{1+dif}'
            else:
                return f'{1+dif}/{n-dif}'
        n += 1
        total = (n * (n+1))//2

print(find_nst())

# 계산 대신 +
def find_nst():
    X = int(input())
    n = total = 1
    while True:
        dif = total - X
        if dif >= 0:
            if n%2 == 0:
                return f'{n-dif}/{1+dif}'
            else:
                return f'{1+dif}/{n-dif}'
        n += 1
        total += n

print(find_nst())

# 짧게
def find_nst():
    X = int(input())
    n = total = 1
    while True:
        dif = total - X
        if dif >= 0:
            return f'{n-dif}/{1+dif}' if n%2 == 0 else f'{1+dif}/{n-dif}'
        n += 1
        total += n

print(find_nst())

# dif 안으로
def find_nst():
    X = int(input())
    n = total = 1
    while True:
        if total >= X:
            dif = total - X
            return f'{n-dif}/{1+dif}' if n%2 == 0 else f'{1+dif}/{n-dif}'
        n += 1
        total += n

print(find_nst())

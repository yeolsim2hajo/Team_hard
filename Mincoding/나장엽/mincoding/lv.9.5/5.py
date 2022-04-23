arr = list(input().split())

def findUpper(arr):
    cnt = 0
    for i in arr:
        if ord('A') <= ord(i) <= ord('Z'):
            cnt += 1

    return cnt

def findLower(arr):
    cnt = 0
    for i in arr:
        if ord('a') <= ord(i) <= ord('z'):
            cnt += 1
    return cnt


print(f'대문자{findUpper(arr)}개')
print(f'소문자{findLower(arr)}개')
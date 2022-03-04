s = list(input())

def maxIndex(s):
    max = ord('A')
    for i in range(0, len(s)):
        if ord(s[i]) > max:
            max = ord(s[i])

    return chr(max)

def minIndex(s):
    min = ord('A')
    for i in range(0, len(s)):
        if ord(s[i]) < min:
            min = ord(s[i])
    return chr(min)



for i in range(0, len(s)):
    if s[i] == maxIndex(s):
        print(i)

for i in range(0, len(s)):
    if s[i] == minIndex(s):
        print(i)
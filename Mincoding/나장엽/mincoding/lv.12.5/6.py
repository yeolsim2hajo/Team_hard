def main():
    string = list(input())
    length = len(string)
    target = string[-1]
    cnt = 0
    for i in range(len(string)):
        if string[i] == target:
            cnt += 1
    print(length)
    print(cnt)
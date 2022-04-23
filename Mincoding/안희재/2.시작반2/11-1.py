def Input():
    arr = list(map(int,input().split()))
    return arr

def main():
    return Input()

def cal(arr):
    sum = 0
    for i in arr:
        sum += i
    return sum

print(cal(main()))
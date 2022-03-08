def INPUT():
    num = int(input())
    return num

def CountDown(x):
    for i in range(x,0,-1):
        print(i,end= ' ')

def main():
    CountDown(INPUT())

main()
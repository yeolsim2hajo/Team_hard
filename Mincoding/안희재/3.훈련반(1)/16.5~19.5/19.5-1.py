nums = list(map(int,input().split()))


def BBQ(lst):
    Max = max(lst)
    Min = min(lst)
    return [Max, Min]

def main(x,y):
    print(f'a={x}')
    print(f'b={y}')


main(BBQ(nums)[0],BBQ(nums)[1])

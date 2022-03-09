num = int(input())
arr = [num-i for i in range(5)]

def KFC():
    print(''.join(map(str,arr)))

KFC()
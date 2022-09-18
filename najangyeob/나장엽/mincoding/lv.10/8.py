def main():
    stone = int(input())
    ret = pingpong(stone)
    print(ret)
    
def pingpong(n):
    tong = n
    tong += 10
    return tong

main()
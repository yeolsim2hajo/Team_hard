a = (input())
b = (input())
# 내장함수 쓰면 금방이긴 한데.. 그냥 해보고 싶었음.ㅎㅎ;;;;;
# 또한, 재귀 씀으로 인해 생기는 메모리 용량 문제도..

def bin_to_dec(str):
    x = 1
    sum = 0
    for i in range(len(str)-1,-1,-1):
        sum += int(str[i]) * x
        x *= 2
    return sum

result1 = bin_to_dec(a) * bin_to_dec(b)

# 하.. 다시 이진수 만드는거 만들어야 하네.. 때려치까..
def dec_to_bin(num):
    if num <= 1:
        return str(num)
    else:
        return str(dec_to_bin(num//2)) + str(num%2)

result2 = dec_to_bin(result1)

print(result2)
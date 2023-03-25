#230325
# height, duration = map(int, input().split())
# binary = ''
# while height:
#     binary += str(height%2)
#     height //= 2
#
# def xor(bin_num):
#     six = '110'
#     length = len(bin_num)
#     answer = ''
#     min_num = min(length, 3)
#     for i in range(-1, -min_num-1, -1):
#         if six[i] == bin_num[i]:
#             answer += '0'
#         else:
#             answer += '1'
#     if min_num == length:
#         return '1'*(3-length) + answer[::-1]
#     return bin_num[:-3] + answer[::-1]
#
# binary = binary[::-1]
# for _ in range(duration):
#     if binary == '':
#         binary = '0'
#     if binary[-1] == '1':
#         binary = xor(binary+'0')
#     else:
#         binary = xor(binary[:-1] or '0')
# two = 1
# length = len(binary)
# for i in range(length-1, -1, -1):
#     if binary[i] == '1':
#         height += two
#     two *= 2
# print(height)


#
def to_binary():
    global height
    binary = ''
    while height:
        binary += str(height%2)
        height //= 2
    return binary[::-1]

def xor(bin_num):
    six = '110'
    length = len(bin_num)
    answer = ''
    min_num = min(length, 3)
    for i in range(-1, -min_num-1, -1):
        if six[i] == bin_num[i]:
            answer += '0'
        else:
            answer += '1'
    if min_num == length:
        return '1'*(3-length) + answer[::-1]
    return bin_num[:-3] + answer[::-1]

def to_decimal():
    two = 1
    length = len(binary)
    height = 0
    for i in range(length-1, -1, -1):
        if binary[i] == '1':
            height += two
        two *= 2
    return height

height, duration = map(int, input().split())
binary = to_binary()
for _ in range(duration):
    if binary == '':
        binary = '0'
    if binary[-1] == '1':
        binary = xor(binary+'0')
    else:
        binary = xor(binary[:-1] or '0')
print(to_decimal())
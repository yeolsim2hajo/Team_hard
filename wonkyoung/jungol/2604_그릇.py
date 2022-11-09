#221109
# dishes = input()
# length = len(dishes)
# pre = dishes[0]
# height = 10
# for i in range(1, length):
#     if pre == dishes[i]:
#         height += 5
#     else:
#         height += 10
#     pre = dishes[i]
# print(height)


# 함수
def find_height():
    dishes = input()
    length = len(dishes)
    pre = dishes[0]
    height = 10
    for i in range(1, length):
        if pre == dishes[i]:
            height += 5
        else:
            height += 10
        pre = dishes[i]
    return height
print(find_height())
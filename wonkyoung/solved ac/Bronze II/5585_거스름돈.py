#230313
# price = 1000 - int(input())
# remain_list = [500, 100, 50, 10, 5]
# cnt = 0
# for remain in remain_list:
#     cnt += price//remain
#     price %= remain
# cnt += price
# print(cnt)

#
price = 1000 - int(input())
remain_list = [500, 100, 50, 10, 5]
def div_price(num):
    global price
    answer = price // num
    price %= num
    return answer
cnt = sum(map(div_price, remain_list))
print(cnt+price)
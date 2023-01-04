#230104
# N = int(input())
# call_list = list(map(int, input().split()))
# youngsik = minsik = 0
# for call in call_list:
#     youngsik += (call//30 + 1) * 10
#     minsik += (call//60 + 1) * 15
# if youngsik < minsik:
#     print('Y', youngsik)
# elif youngsik > minsik:
#     print('M', minsik)
# else:
#     print('Y', 'M', minsik)


# 수정
# N = int(input())
# call_list = list(map(int, input().split()))
# price = {'Y':0, 'M':0}
# for call in call_list:
#     price['Y'] += (call//30 + 1) * 10
#     price['M'] += (call//60 + 1) * 15
# another_key = ''
# if price['Y'] == price['M']:
#     key, another_key = 'Y M', 'Y'
# elif price['Y'] < price['M']:
#     key = 'Y'
# else:
#     key = 'M'
# print(key, price[another_key or key])


# 함수형 - 시간 더 걸림
# N = int(input())
# call_list = list(map(int, input().split()))
# price = {'Y':0, 'M':0}
# def calc_price():
#     for call in call_list:
#         price['Y'] += (call//30 + 1) * 10
#         price['M'] += (call//60 + 1) * 15
#
# def find_key():
#     another_key = ''
#     if price['Y'] == price['M']:
#         key, another_key = 'Y M', 'Y'
#     elif price['Y'] < price['M']:
#         key = 'Y'
#     else:
#         key = 'M'
#     return f'{key} {price[another_key or key]}'
#
# calc_price()
# print(find_key())


#
N = int(input())
call_list = list(map(int, input().split()))
price = {'Y':0, 'M':0}
def calc_price():
    for call in call_list:
        price['Y'] += (call//30 + 1) * 10
        price['M'] += (call//60 + 1) * 15

def find_key():
    another_key = ''
    if price['Y'] == price['M']:
        key, another_key = 'Y M', 'Y'
    elif price['Y'] < price['M']:
        key = 'Y'
    else:
        key = 'M'
    print(key, price[another_key or key])

calc_price()
find_key()
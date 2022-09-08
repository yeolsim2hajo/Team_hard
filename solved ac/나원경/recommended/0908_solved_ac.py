#13305 주유소
# N = int(input())
# road = list(map(int, input().split()))
# price = list(map(int, input().split()))
# total_price, total_road, min_price = 0, road[0], price[0]
# for i in range(1,N-1):
#     if price[i] < min_price:
#         total_price += min_price*total_road
#         min_price = price[i]
#         total_road = road[i]
#     else:
#         total_road += road[i]
# total_price += min_price*total_road
# print(total_price)


# 함수로
# def find_sum():
#     N = int(input())
#     road = list(map(int, input().split()))
#     price = list(map(int, input().split()))
#     total_price, total_road, min_price = 0, road[0], price[0]
#     for i in range(1,N-1):
#         if price[i] < min_price:
#             total_price += min_price*total_road
#             min_price = price[i]
#             total_road = road[i]
#         else:
#             total_road += road[i]
#     total_price += min_price*total_road
#     print(total_price)
# find_sum()


# print -> return
# def find_sum():
#     N = int(input())
#     road = list(map(int, input().split()))
#     price = list(map(int, input().split()))
#     total_price, total_road, min_price = 0, road[0], price[0]
#     for i in range(1,N-1):
#         if price[i] < min_price:
#             total_price += min_price*total_road
#             min_price = price[i]
#             total_road = road[i]
#         else:
#             total_road += road[i]
#     total_price += min_price*total_road
#     return total_price
# print(find_sum())
#230202
N = int(input())
prices = set()
delivery_acc, cnt = {}, {}
for i in range(N):
    price, delivery = map(int, input().split())
    prices.add(price)
    if delivery_acc.get(price, -1) != -1:
        delivery_acc[price] += delivery
        cnt[price] += 1
    else:
        delivery_acc[price] = delivery
        cnt[price] = 1

prices = sorted(prices)
total_values = sum(delivery_acc.values())
for price in prices:
    total_values, delivery_acc[price] = total_values - delivery_acc[price],total_values

max_val = determined = 0
now_cnt = N
for price in prices:
    now_val = price * now_cnt - delivery_acc[price]
    print(price, now_val, now_cnt)
    # print(price, now_val)
    if max_val < now_val:
        max_val = now_val
        determined = price
    elif max_val == now_val and determined > price:
        determined = price
    now_cnt -= cnt[price]
print(delivery_acc)
print(determined)




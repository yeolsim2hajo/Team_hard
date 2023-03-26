#230326
# E, S, M = map(int, input().split())
# year = 0
# while True:
#     if year%28 + 1 == S and year%19 + 1 == M and year%15 + 1 == E:
#         print(year+1)
#         break
#     year += 1


#
def calc_year():
    E, S, M = map(int, input().split())
    year = 0
    while True:
        if year % 28 + 1 == S and year % 19 + 1 == M and year % 15 + 1 == E:
            return year + 1
        year += 1
print(calc_year())
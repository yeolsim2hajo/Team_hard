Month, D, Y, T = input().split()
D = int(D[:-1])
Y = int(Y)
H, M = map(int, T.split(':'))
month_name_li = ["January" , "February", "March", "April", "May", "June", 
            "July", "August", "September", "October", "November", "December"]
month_day_li = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
if Y%400 == 0 or (Y%4 == 0 and Y%100 != 0):
    month_day_li[1] += 1
total_time = sum(month_day_li) * 24 * 60

last_month_idx = month_name_li.index(Month)
current_time = (sum(month_day_li[:last_month_idx]) + D-1)*24*60 + H*60 + M
print(current_time/total_time * 100)
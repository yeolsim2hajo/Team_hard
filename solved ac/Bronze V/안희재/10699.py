import datetime

today = datetime.datetime.now()
print(today.date()) # .date 하면 날짜만 취득


# -----------------------------
#dt_now = datetime.datetime.now()
#print(dt_now)
# 2020-09-02 15:13:29.383069

# 날짜만 취득
#print(dt_now.date())
# 2020-09-02

# 년도 취득
#print(dt_now.year)
# 2020

# 월 취득
#print(dt_now.month)
# 9

# 일 취득
#print(dt_now.day)
# 2

# 시간만 취득
#print(dt_now.time())
# 15:13:29.383069

# 시 취득
#print(dt_now.hour)
# 15

# 분  취득
#print(dt_now.minute)
# 13

# 초 취득
#print(dt_now.second)
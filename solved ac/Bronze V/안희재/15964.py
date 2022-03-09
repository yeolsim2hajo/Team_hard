from datetime import date

ans = date.today()

print(ans.year)
print(ans.month)
print(ans.day)

# 세계 표준시 구하는 문제 -> datetime import해와서, datetime.datime.utcnw()!

# 아래처럼 풀 수 없음, ans의 타입은 <class 'datetime.datetime'>. 야매 컷, 정공법 ㄱ
# -----------------
# import datetime
# ans = datetime.datetime.utcnow()

# print(ans[0:4])
# print(ans[5:7])
# print(ans[9:11])
# -----------------
# https://velog.io/@swhan9404/python-%EC%9D%98-%EC%8B%9C%EA%B0%84-%EB%8B%A4%EB%A3%A8%EA%B8%B0

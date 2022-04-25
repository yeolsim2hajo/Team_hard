import datetime

month = int(input())
day = int(input())

def findDay(a, b):
    day = ["MON","TUE","WED","THU","FRI","SAT","SUN"]
    return day[datetime.date(2020, a, b).weekday()]

print(findDay(month, day))


# https://docs.python.org/ko/3/library/datetime.html
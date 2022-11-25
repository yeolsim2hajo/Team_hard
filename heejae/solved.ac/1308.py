from datetime import datetime

def get_1000_year_day(start_year):
    year_day_1000 = 0
    
    for year in range(start_year, start_year + 1000):
        if year % 400 == 0:
            year_day_1000 += 366
        elif year % 100 == 0:
            year_day_1000 += 365
        elif year % 4 == 0:
            year_day_1000 += 366
        else:
            year_day_1000 += 365
            
    return year_day_1000
            


def d_day(today, dday):
    today_date = datetime(year=today[0], month=today[1], day=today[2])
    dday_date = datetime(year=dday[0], month=dday[1], day=dday[2])
    
    dday_day = (dday_date - today_date).days
    
    year_day_1000 = get_1000_year_day(start_year=today[0])
    
    if dday_day >= year_day_1000:
        dday_day = "gg"
    else:
        dday_day = f"D-{dday_day}"
    
    return dday_day


if __name__ == "__main__":
    today = list(map(int, input().split()))
    dday = list(map(int, input().split()))
    print(d_day(today, dday))
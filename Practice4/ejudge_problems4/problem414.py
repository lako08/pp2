from datetime import datetime, timedelta
import re

def parse_moment(s):
    date_part, tz_part = s.split(' UTC')
    year, month, day = map(int, date_part.split('-'))
    
    sign = 1 if tz_part[0] == '+' else -1
    hours, minutes = map(int, tz_part[1:].split(':'))
    
    offset = timedelta(hours=sign * hours, minutes=sign * minutes)
    
    dt = datetime(year, month, day)
    dt_utc = dt - offset
    
    return dt_utc

dt1 = parse_moment(input().strip())
dt2 = parse_moment(input().strip())

diff = abs((dt2 - dt1).total_seconds())
days = int(diff // 86400)

print(days)
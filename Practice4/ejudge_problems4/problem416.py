from datetime import datetime, timedelta
import re

def parse_moment(s):
    date_part, time_part, tz_part = s.split(' ')
    year, month, day = map(int, date_part.split('-'))
    hour, minute, second = map(int, time_part.split(':'))
    
    sign = 1 if tz_part[3] == '+' else -1
    tz_hours, tz_minutes = map(int, tz_part[4:].split(':'))
    
    offset = timedelta(hours=sign * tz_hours, minutes=sign * tz_minutes)
    
    dt = datetime(year, month, day, hour, minute, second)
    dt_utc = dt - offset
    
    return dt_utc

start_str = input().strip()
end_str = input().strip()

start_utc = parse_moment(start_str)
end_utc = parse_moment(end_str)

duration = int((end_utc - start_utc).total_seconds())

print(duration)
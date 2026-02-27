#1
from datetime import datetime, timedelta

today = datetime.now()
new_date = today - timedelta(days=5)

print("Today:", today)
print("5 days ago:", new_date)


#2
from datetime import datetime, timedelta

today = datetime.now().date()

yesterday = today - timedelta(days=1)
tomorrow = today + timedelta(days=1)

print("Yesterday:", yesterday)
print("Today:", today)
print("Tomorrow:", tomorrow)

#3
from datetime import datetime

now = datetime.now()
without_microseconds = now.replace(microsecond=0)

print("With microseconds:", now)
print("Without microseconds:", without_microseconds)

#4
from datetime import datetime

date1 = datetime(2026, 2, 20, 10, 0, 0)
date2 = datetime(2026, 2, 27, 12, 30, 0)

difference = date2 - date1
seconds = difference.total_seconds()

print("Difference in seconds:", seconds)
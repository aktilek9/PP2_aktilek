import datetime

# 1
x = datetime.date.today()
print(x - datetime.timedelta(days=5))

# 2
x = datetime.date.today()
print(x - datetime.timedelta(days=1))
print(x)
print(x + datetime.timedelta(days=1))


# 3
date = datetime.datetime.now()
date = date.replace(microsecond=0)

print(date)


# 4
date1 = datetime.datetime(2026, 9, 27, 10, 0)
date2 = datetime.datetime(2026, 9, 27, 13, 30)

diff = date2 - date1
print(diff.total_seconds())
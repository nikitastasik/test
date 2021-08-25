from datetime import datetime
from datetime import date
from datetime import time
from datetime import timedelta

d1 = date(2019, 3, 12)
print(d1)
print(d1.year)
print(d1.month)
print(d1.day)
print()
t1 = time(23, 10, 59)
print(t1)
print(t1.hour)
print(t1.minute)
print(t1.second)
print()
print(date.today())
print()

dt = datetime(2019, 3, 12, 12, 12, 12)
print(dt)
print()

print(dt.year)
print()

now = datetime.now()
print(now)
print(now.month)
print()

new_dt = now.replace(year=2019) #return new obj
print(new_dt)
print()

dt2 = datetime.strptime('30/08/2018', '%d/%m/%Y')
print(dt2)

dt3 = datetime.strptime('29/03/2019 10:40', '%d/%m/%Y %H:%M')
print(dt3)

dt4 = datetime.strptime('06-28-2017 09:20', '%m-%d-%Y %H:%M')
print(dt4)

dt5 = datetime.strptime('2016-06-09', '%Y-%m-%d')
print(dt5)

import locale
print()
print(locale.setlocale(locale.LC_ALL, ''))
now2 = datetime.now()
print(now.strftime('%Y-%m-%d (%a)'))
print(now.strftime('%Y-%B-%d число (%A)'))

delta1 = timedelta(days=3, hours=2, minutes=10)
print(delta1)

delta2 = timedelta(days=2, hours=1, minutes=5)
print(delta1 - delta2)
print(delta2 - delta1)

my_birthday = date(1998, 8, 7)

delta3 = date.today() - my_birthday
print(int(delta3.days / 365))

wife_birthday = date(1990, 9, 6)
am_i_older = my_birthday < wife_birthday
print(am_i_older)


def datetime():
    return None
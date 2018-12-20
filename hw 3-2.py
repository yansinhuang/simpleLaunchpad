import datetime
lst_date1 = [int(i) for i in input().split()]
d = int(input())

date1 = datetime.datetime(lst_date1[0], lst_date1[1], lst_date1[2])

print((date1 + datetime.timedelta(days = d)).strftime('%Y-%m-%d'))

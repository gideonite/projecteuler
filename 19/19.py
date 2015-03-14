months = ["January",
          "February",
          "March",
          "April",
          "May",
          "June",
          "July",
          "August",
          "September",
          "October",
          "November",
          "December"]

months_to_days = {"January": 31,
          "February": 28,
          "March":31,
          "April": 30,
          "May":31,
          "June": 30,
          "July":31,
          "August":31,
          "September": 30,
          "October":31,
          "November": 30,
          "December":31}

def is_leap_year(year):
  if year % 4 != 0:
    return False
  elif year % 100 != 0:
    return True
  elif year % 400 != 0:
    return False
  else:
    return True

def inc_month(month):
  ret = month+1
  return ret % 12

def inc_day_of_week(day_of_week):
  ret = day_of_week+1
  return ret % 7

def month_to_days(month, year):
  if month == 1 and is_leap_year(year):
    return 29
  else:
    return months_to_days[months[month]]

# Jan 1, 1900 was a Monday

sunday_count = 0
curr_year = 1900
curr_month = 0
curr_day_of_month = 1
curr_day_of_week = 0  # Monday is first day of week.
while True:
  if curr_year >= 1901 and curr_day_of_week == 6 and curr_day_of_month == 1:
    sunday_count+=1

  if curr_year == 2000 and curr_month == 11 and curr_day_of_month == 31:
    break
  else:
    curr_day_of_month+=1
    days_in_month = month_to_days(curr_month, curr_year)
    if curr_day_of_month > days_in_month:
      curr_month = inc_month(curr_month)
      curr_day_of_month = 1
    if curr_month == 1 and curr_day_of_month == 1:
      curr_year+=1
    curr_day_of_week = inc_day_of_week(curr_day_of_week)

sunday_count

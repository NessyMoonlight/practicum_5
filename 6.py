day1 = int(input())
day2 = int(input())
day3 = int(input())

count_recurring_days = 1
if day1 == day2:
    count_recurring_days += 1
if day1 == day3:
    count_recurring_days += 1
if day2 == day3:
    count_recurring_days += 1
if count_recurring_days == 4:
    count_recurring_days -= 1

print(count_recurring_days)
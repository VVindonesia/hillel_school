total_seconds = int(input())
days_number, remainder_from_seconds = divmod(total_seconds, 24*60*60)
hours_number, remainder_from_seconds = divmod(remainder_from_seconds, 60*60)
minutes_number, seconds_number = divmod(remainder_from_seconds, 60)
time1 = f"{str(hours_number).zfill(2)}:{str(minutes_number).zfill(2)}:{str(seconds_number).zfill(2)}"
if days_number %10 == 1 and days_number % 100 !=11:
    time2 = "1 день"
elif days_number %10 in (2, 3, 4) and days_number %100 not in (12, 13 ,14) :
    time2 = f"{days_number} дня"
else:
    time2 = f"{days_number} дней"
time3 = f"{time2}, {time1}"
print(time3)

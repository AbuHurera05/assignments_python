from datetime import *
# Qno1
# dob_str = input("Enter your date of birth (YYYY-MM-DD):")
# dob = datetime.strptime(dob_str,"%Y-%m-%d").date()
# today = datetime.today().date()
# print(today)
# days = (today-dob).days
# second = (today-dob).total_seconds()
# print(f"Days: {days}, Seconds: {second}")

# Qno2
# event_date = input("Enter your upcoming event date (YYYY-MM-DD HH:MM)")
# event_date = datetime.strptime(event_date,"%Y-%m-%d %H:%M")
# now = datetime.now()
# time_left = event_date - now
# days = time_left.days
# hours = time_left.seconds // 3600
# minutes = (time_left.seconds % 3600)//60
# print(f"Time left for the event: {days} days, {hours} hours, {minutes} minutes")

# Qno3
from datetime import datetime

date_input = input("Enter a date (YYYY-MM-DD): ")
date_obj = datetime.strptime(date_input, "%Y-%m-%d")

day = date_obj.day
month = date_obj.strftime("%B")
year = date_obj.year

# Add suffix to day (st, nd, rd, th)
if 4 <= day <= 20 or 24 <= day <= 30:
    suffix = "th"
else:
    suffix = ["st", "nd", "rd"][day % 10 - 1]

print(f"{day}{suffix} {month}, {year}")



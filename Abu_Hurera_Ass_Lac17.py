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
# from datetime import datetime

# date_input = input("Enter a date (YYYY-MM-DD): ")
# date_obj = datetime.strptime(date_input, "%Y-%m-%d")

# day = date_obj.day
# month = date_obj.strftime("%B")
# year = date_obj.year

# # Add suffix to day (st, nd, rd, th)
# if 4 <= day <= 20 or 24 <= day <= 30:
#     suffix = "th"
# else:
#     suffix = ["st", "nd", "rd"][day % 10 - 1]

# print(f"{day}{suffix} {month}, {year}")

# Qno4
# dob_input = input("Enter your date of birth (YYYY-MM-DD): ")
# dob = datetime.strptime(dob_input, "%Y-%m-%d")
# today = datetime.now()

# if dob > today:
#     print("Error: Future date entered! Please enter a valid date of birth.")
# else:
#     age_days = (today - dob).days
#     print(f"Your age in days: {age_days}")

# Qno5
# t1 = input("Enter first time (HH:MM:SS): ")
# t2 = input("Enter second time (HH:MM:SS): ")

# fmt = "%H:%M:%S"
# time1 = datetime.strptime(t1, fmt)
# time2 = datetime.strptime(t2, fmt)

# diff = abs(time2 - time1)
# hours = diff.seconds // 3600
# minutes = (diff.seconds % 3600) // 60

# print(f"Time difference: {hours} hours and {minutes} minutes")

# Qno6
# dob = datetime.strptime(input("Enter your DOB (YYYY-MM-DD): "), "%Y-%m-%d")
# target_date = datetime.strptime(input("Enter the date you want to check age on (YYYY-MM-DD): "), "%Y-%m-%d")

# if target_date < dob:
#     print("Invalid: Target date is before your birth.")
# else:
#     age_years = target_date.year - dob.year - ((target_date.month, target_date.day) < (dob.month, dob.day))
#     print(f"Your age on {target_date.strftime('%d %B %Y')} will be {age_years} years.")

# QNo7


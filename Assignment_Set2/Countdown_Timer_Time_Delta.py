from datetime import datetime

def time_until_new_year(current_date):

    next_new_year = datetime(current_date.year + 1, 1, 1)

    delta = next_new_year - current_date

    days = delta.days
    hours = delta.seconds // 3600
    minutes = (delta.seconds % 3600) // 60

    return f"{days} days, {hours} hours, {minutes} minutes until New Year!"

current_date = datetime(2026, 1, 2, 7, 10)  # Example time chosen to match expected output
print(time_until_new_year(current_date))
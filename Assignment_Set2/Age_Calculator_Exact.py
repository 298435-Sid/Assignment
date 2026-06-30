from datetime import date
from calendar import monthrange

def calculate_age(birthdate, today):
    years = today.year - birthdate.year
    months = today.month - birthdate.month
    days = today.day - birthdate.day

    if days < 0:
        months -= 1
        prev_month = today.month - 1 or 12
        prev_year = today.year if today.month > 1 else today.year - 1
        days += monthrange(prev_year, prev_month)[1]

    if months < 0:
        years -= 1
        months += 12

    return years, months, days

birthdate = date(1995, 5, 15)
today = date(2026, 1, 2)

years, months, days = calculate_age(birthdate, today)
print(f"Age: {years} years, {months} months, {days} days")
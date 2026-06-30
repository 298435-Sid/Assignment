from datetime import datetime, timedelta

def add_business_days(start_date, n):
    current_date = start_date
    days_added = 0

    while days_added < n:
        current_date += timedelta(days=1)

        if current_date.weekday() < 5:
            days_added += 1

    return current_date

start = datetime(2026, 1, 2)  
result = add_business_days(start, 5)

print(result.strftime("%A, %Y-%m-%d"))
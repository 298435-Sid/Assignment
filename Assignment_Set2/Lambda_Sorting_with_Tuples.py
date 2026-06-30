employees = [
    ("Alice", 30, 50000),
    ("Bob", 25, 75000),
    ("Charlie", 35, 60000)
]

sorted_employees = sorted(employees, key=lambda emp: emp[2], reverse=True)

print(sorted_employees)
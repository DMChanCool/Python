"""
Create a simple expense tracking program that allows users to record and query their daily expenses.

Features (功能):
1. Add new expense records
2. Query total expenses for a specific date
3. Show sum of all records

Terminal Execution Results (終端機執行結果):
1. Add new expense record
2. Query expenses for a specific date
3. Show total of all records
4. Exit system
Please enter function number:1
Please enter date:2024-01-01
Please enter amount:100
1. Add new expense record
2. Query expenses for a specific date
3. Show total of all records
4. Exit system
Please enter function number:1
Please enter date:2024-01-01
Please enter amount:200
1. Add new expense record
2. Query expenses for a specific date
3. Show total of all records
4. Exit system
Please enter function number:2
Please enter date:2024-01-01
Total expenses for 2024-01-01 is 300
1. Add new expense record
2. Query expenses for a specific date
3. Show total of all records
4. Exit system
Please enter function number:3
Total of all records is 300
1. Add new expense record
2. Query expenses for a specific date
3. Show total of all records
4. Exit system
Please enter function number:4
"""


def add_expense(records, date, amount):
    if date in records:
        records[date] += amount
    else:
        records[date] = amount


def query_expense(records, date):
    if date in records:
        return records[date]
    else:
        return 0


def show_total(records):
    return sum(records.values())


records = {}
while True:
    print("1.add new expense record")
    print("2.query expenses for a specific date")
    print("3.show total of all records")
    print("4.exit system")
    function_number = input("Please enter function number:")

    if function_number == "1":
        date = input("Please enter date(YYYY-MM-DD):")
        amount = int(input("Please enter amount:"))
        add_expense(records, date, amount)

    elif function_number == "2":
        date = input("Please enter date:")
        total = query_expense(records, date)
        print(f"total xpenses for {date} is {total}")

    elif function_number == "3":
        total = show_total(records)
        print(f"total of all records is {total}")
    elif function_number == "4":
        break
    else:
        print("Wrong input")
        continue

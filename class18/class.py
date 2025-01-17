# 新增支出紀錄的函式
# Function to add a new expense record
def add_expense(records, date, amount):
    # 檢查日期是否已經存在於紀錄中
    # Check if the date already exists in records
    if date in records:
        # 如果日期存在，就把新金額加到現有金額上
        # If date exists, add new amount to existing amount
        records[date] += amount
    else:
        # 如果是新的日期，就建立新的紀錄
        # If it's a new date, create a new record
        records[date] = amount


# 查詢特定日期支出的函式
# Function to query expenses for a specific date
def query_expense(records, date):
    # 檢查要查詢的日期是否存在
    # Check if the date exists in records
    if date in records:
        # 如果日期存在，回傳該日期的支出金額
        # If date exists, return the expense amount
        return records[date]
    else:
        # 如果日期不存在，回傳0元
        # If date doesn't exist, return 0
        return 0


# 計算所有支出總和的函式
# Function to calculate total of all expenses
def show_total(records):
    # 把所有日期的支出加起來
    # Add up all expenses from all dates
    return sum(records.values())


# 建立一個空的字典來儲存所有支出紀錄
# Create an empty dictionary to store all expense records
records = {}

# 主程式迴圈，會一直執行直到使用者選擇退出
# Main program loop, continues until user chooses to exit
while True:
    # 顯示功能選單
    # Display menu options
    print("1. Add new expense record")
    print("2. Query expenses for a specific date")
    print("3. Show total of all records")
    print("4. Exit system")
    function_number = input("Please enter function number:")

    # 根據使用者的選擇執行不同功能
    # Execute different functions based on user's choice
    if function_number == "1":
        # 選項1：新增支出紀錄
        # Option 1: Add new expense record
        date = input("Please enter date (YYYY-MM-DD):")
        amount = int(input("Please enter amount:"))
        add_expense(records, date, amount)
    elif function_number == "2":
        # 選項2：查詢特定日期的支出
        # Option 2: Query expenses for a specific date
        date = input("Please enter date (YYYY-MM-DD):")
        total = query_expense(records, date)
        print(f"Total expenses for {date} is {total}")
    elif function_number == "3":
        # 選項3：顯示所有支出總和
        # Option 3: Show total of all expenses
        total = show_total(records)
        print(f"Total of all records is {total}")
    elif function_number == "4":
        # 選項4：離開系統
        # Option 4: Exit system
        break
    else:
        # 如果輸入無效的選項號碼
        # If invalid option number is entered
        print("Invalid function number. Please try again.")

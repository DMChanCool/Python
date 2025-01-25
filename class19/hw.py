"""
小小記帳程式 - 升級版！
Mini Expense Tracker - Upgraded Version!

功能說明 (Features):
1. 可以記錄每天的支出 (Record daily expenses)
2. 可以查詢特定日期的支出 (Query expenses for specific dates)
3. 可以顯示總支出 (Show total expenses)
4. 可以查詢最近N天的支出 (Query recent N days expenses)
5. 支援多種日期輸入格式 (Support multiple date input formats)
6. 記帳資料會自動儲存，下次開啟時可以繼續使用 (Data is saved and can be loaded next time)

注意事項:
- 日期格式可以是: "2024-01-01" 或 "2024/01/01" 或 "20240101"
- 金額必須是整數
- 所有資料會存在 expenses.txt 檔案中

Notes:
- Date formats can be: "2024-01-01" or "2024/01/01" or "20240101"
- Amount must be an integer
- All data will be saved in expenses.txt file

終端機執行結果範例 (Example Terminal Output):
---
歡迎使用小小記帳程式！(Welcome to Mini Expense Tracker!)

1. 新增支出紀錄 (Add new expense)
2. 查詢日期支出 (Query date expenses)
3. 顯示總支出 (Show total expenses)
4. 查詢近期支出 (Query recent expenses)
5. 離開程式 (Exit)
請選擇功能 (Select function): 1

請輸入日期 (Enter date): 2024-01-01
請輸入金額 (Enter amount): 100
已儲存支出紀錄！(Expense record saved!)

1. 新增支出紀錄 (Add new expense)
2. 查詢日期支出 (Query date expenses)
3. 顯示總支出 (Show total expenses)
4. 查詢近期支出 (Query recent expenses)
5. 離開程式 (Exit)
請選擇功能 (Select function): 1

請輸入日期 (Enter date): 20240101
請輸入金額 (Enter amount): 200
已儲存支出紀錄！(Expense record saved!)

1. 新增支出紀錄 (Add new expense)
2. 查詢日期支出 (Query date expenses)
3. 顯示總支出 (Show total expenses)
4. 查詢近期支出 (Query recent expenses)
5. 離開程式 (Exit)
請選擇功能 (Select function): 2

請輸入要查詢的日期 (Enter date to query): 2024/01/01
2024-01-01 的支出為: 300 元 (Expenses for 2024-01-01: 300)

1. 新增支出紀錄 (Add new expense)
2. 查詢日期支出 (Query date expenses)
3. 顯示總支出 (Show total expenses)
4. 查詢近期支出 (Query recent expenses)
5. 離開程式 (Exit)
請選擇功能 (Select function): 3

總支出為: 300 元 (Total expenses: 300)

1. 新增支出紀錄 (Add new expense)
2. 查詢日期支出 (Query date expenses)
3. 顯示總支出 (Show total expenses)
4. 查詢近期支出 (Query recent expenses)
5. 離開程式 (Exit)
請選擇功能 (Select function): 4

請問要查詢最近幾天的支出？(How many recent days to query?): 7
從 2024-01-01 到 2024-01-07 的總支出為: 500 元
詳細資料：
2024-01-01: 300 元
2024-01-03: 200 元
(Total expenses from 2024-01-01 to 2024-01-07: 500
Details:
2024-01-01: 300
2024-01-03: 200)

1. 新增支出紀錄 (Add new expense)
2. 查詢日期支出 (Query date expenses)
3. 顯示總支出 (Show total expenses)
4. 查詢近期支出 (Query recent expenses)
5. 離開程式 (Exit)
請選擇功能 (Select function): 5

謝謝使用！資料已儲存。(Thank you! Data has been saved.)
"""

import datetime
import os


def format_date(date_str):
    """將不同格式的日期字串轉換成統一格式 (Convert different date formats to a standard format)"""
    try:
        # 移除所有的 - 或 / 並合併
        clean_date = date_str
        if "-" in date_str:
            clean_date = "".join(date_str.split("-"))
        elif "/" in date_str:
            clean_date = "".join(date_str.split("/"))

        # 確保日期字串長度為8位
        if len(clean_date) != 8:
            return None

        # 轉換成日期物件
        date = datetime.datetime.strptime(clean_date, "%Y%m%d")
        # 回傳統一格式
        return date.strftime("%Y-%m-%d")
    except:
        return None


def load_expenses():
    """載入記帳檔案 (Load expense records)"""
    expenses = {}
    if os.path.exists("expenses.txt"):
        with open("expenses.txt", "r") as file:
            for line in file:
                date, amount = line.strip().split(",")
                expenses[date] = int(amount)
    return expenses


def save_expenses(expenses):
    """儲存記帳檔案 (Save expense records)"""
    with open("expenses.txt", "w") as file:
        for date, amount in expenses.items():
            file.write(f"{date},{amount}\n")


def add_expense(expenses, date, amount):
    """新增支出紀錄 (Add new expense)"""
    formatted_date = format_date(date)
    if formatted_date:
        if formatted_date in expenses:
            expenses[formatted_date] += amount
        else:
            expenses[formatted_date] = amount
        save_expenses(expenses)
        return True
    return False


def query_expense(expenses, date):
    """查詢特定日期支出 (Query specific date expenses)"""
    formatted_date = format_date(date)
    if formatted_date and formatted_date in expenses:
        return expenses[formatted_date]
    return 0


def show_total(expenses):
    """計算總支出 (Calculate total expenses)"""
    return sum(expenses.values())


def query_recent_expenses(expenses, days):
    """查詢最近N天的支出 (Query recent N days expenses)"""
    today = datetime.datetime.now()
    start_date = today - datetime.timedelta(days=days - 1)

    # 篩選日期範圍內的支出
    recent_expenses = {}
    for date_str, amount in expenses.items():
        date = datetime.datetime.strptime(date_str, "%Y-%m-%d")
        if start_date.date() <= date.date() <= today.date():
            recent_expenses[date_str] = amount

    return recent_expenses


# 主程式 (Main program)
expenses = load_expenses()

print("歡迎使用小小記帳程式！(Welcome to Mini Expense Tracker!)\n")

while True:
    print("\n1. 新增支出紀錄 (Add new expense)")
    print("2. 查詢日期支出 (Query date expenses)")
    print("3. 顯示總支出 (Show total expenses)")
    print("4. 查詢近期支出 (Query recent expenses)")
    print("5. 離開程式 (Exit)")
    choice = input("請選擇功能 (Select function): ")

    if choice == "1":
        date = input("\n請輸入日期 (Enter date): ")
        try:
            amount = int(input("請輸入金額 (Enter amount): "))
            if add_expense(expenses, date, amount):
                print("已儲存支出紀錄！(Expense record saved!)")
            else:
                print("日期格式錯誤！(Invalid date format!)")
        except:
            print("金額必須是整數！(Amount must be an integer!)")

    elif choice == "2":
        date = input("\n請輸入要查詢的日期 (Enter date to query): ")
        total = query_expense(expenses, date)
        formatted_date = format_date(date)
        if formatted_date:
            print(
                f"{formatted_date} 的支出為: {total} 元 (Expenses for {formatted_date}: {total})"
            )
        else:
            print("日期格式錯誤！(Invalid date format!)")

    elif choice == "3":
        total = show_total(expenses)
        print(f"\n總支出為: {total} 元 (Total expenses: {total})")

    elif choice == "4":
        try:
            days = int(
                input("\n請問要查詢最近幾天的支出？(How many recent days to query?): ")
            )
            if days <= 0:
                print("天數必須大於0！(Days must be greater than 0!)")
                continue

            recent_expenses = query_recent_expenses(expenses, days)
            if recent_expenses:
                today = datetime.datetime.now()
                start_date = today - datetime.timedelta(days=days - 1)
                total = sum(recent_expenses.values())

                print(
                    f"從 {start_date.strftime('%Y-%m-%d')} 到 {today.strftime('%Y-%m-%d')} 的總支出為: {total} 元"
                )
                print("詳細資料：")
                for date in sorted(recent_expenses.keys()):
                    print(f"{date}: {recent_expenses[date]} 元")
            else:
                print("此期間沒有支出記錄！(No expenses found in this period!)")
        except:
            print("請輸入有效的天數！(Please enter a valid number of days!)")

    elif choice == "5":
        print("\n謝謝使用！資料已儲存。(Thank you! Data has been saved.)")
        break

    else:
        print("\n請輸入有效的選項！(Please enter a valid option!)")

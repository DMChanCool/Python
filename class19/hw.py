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

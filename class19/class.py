# 附加檔案 - 使用open()函式
# ex:
file = open("class18/file_test.py", "a")
file.write("\nprint('hello python')")
file.close()

# 附加檔案 - 使用with open() as
# ex:
with open("class18/file_test.py", "a") as file:
    file.write("\nprint('hello python')")

# replace - 取代字串中的特定字串
# ex:
text = "hello world"
new_text = text.replace("world", "python")
print(new_text)

# strip - 移除字串前後的空白
# ex:
text = "  hello world  "
new_text = text.strip()
print(new_text)

# split - 依照特定字元分割字串
# ex:
text = "hello,world,python"
words = text.split(",")
print(words)

# zfill - 字串捕0
# ex:
number = "7"
new_number = number.zfill(2)
print(new_number)

# datetime 模組
# datetime模組提供了處理日期、時間的類別和函示

import datetime

# get current date and time- use datetime.datetime.now() function)
# ex:
now = datetime.datetime.now()
print(now)

# 字串轉換成日期- use datetime.datetime.strptime() function)
# ex:
date = datetime.datetime.strptime("2024-01-01", "%Y-%m-%d")
print(date)

# 日期變字串 - 用datetime.datetime.strftime()
# ex:
date = datetime.datetime.now()
date_str = date.strftime("%Y-%m-%d")
print(date_str)

# calculate how many days are left until the target date
# ex:
target_date = datetime.datetime.strptime("2024-01-01", "%Y-%m-%d")
now = datetime.datetime.now()
days_left = (target_date - now).days
print(days_left)

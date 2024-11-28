"""·執行範例： 〔’晴天’,’多雲’,’雨天’,’晴天’,’多雲 請輸入要修改的星期數字
(1、7):a 請輸入數字編號 請輸入要修改的星期數字
(1一7):9 輸入錯誤查無此星期，請重新輸入 請輸入要修改的星期數字
(1、7):6 您要修改的星期是6 原本的天氣是雷陣雨 請輸入新的天氣：晴天 修改後的天氣是晴天 〔’晴天’,’多雲’,’雨天’,’晴天’,’多雲 Maker+Coder=Singular Super Inventor 口口口口口口口口口口口口口口口口 
雷陣雨’ 
晴天 
晴天 
"""

weather = ["晴天", "多雲", "雨天", "晴天", "多雲", "雷陣雨", "晴天"]

print("當前一週的天氣預報:", weather)

while True:
    day = int(input("請輸入要修改的星期數字（1~7): "))

    if 1 <= day <= 7:
        print(f"您要修改的星期是{day} 原本的天氣是{weather[day]}")
        new_weather = input("請輸入新的天氣：")
        weather[day - 1] = new_weather
        print(f"修改後的天氣是{new_weather}")
        print("修改後的一週天氣預報:", weather)
        break
    else:
        print("查無此星期，請重新輸入")

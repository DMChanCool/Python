# list len
L = [1, 2, 3, 4, 5]
print(len(L))  # 取得list的長度，也就是list當中的元素數量
# 務必不要跟index搞混，因為index是取得資料的編號，而len是取得list的數量的方式

for i in range(len(L)):  # i is index here
    print(L[i])

for i in L:  # i 的資料
    print(i)


# 要使用哪一種方式讀取list當中的資料，要看使用的情境當中是否有必要利用index

juice_list = ["蘋果汁", "柳橙汁", "葡萄汁", "系統關閉"]

while True:
    for i in range(len(juice_list)):
        print(f"{i+1}.{juice_list[i]}")

    try:
        select = int(input("請輸入編號:"))
    except:
        print("請輸入數字")
        continue
    if select > len(juice_list):
        print("輸入錯誤查無此果汁，請重新輸入")
        continue
    elif juice_list[select - 1] == "系統關閉":
        print("~~系統關閉~~")
        break
    else:
        print(f"您點的商品是{juice_list[select-1]}")


# 更新list當中的資料
L = [1, 2, 3, 4, 5]
L[0] = 100  # 更新第1個資料
print(L)

# list跟字串很像的地方
# 合併清單資料
L1 = [1, 2, 3]
L2 = [4, 5, 6]
L3 = L1 + L2
print(L3)

# 重複清單資料
L = [1, 2, 3]
L = L * 3
print(L)

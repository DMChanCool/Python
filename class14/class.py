# 新增/修改字典的內容
# (add/modify dictionary content: add new items or change the number of items)
d = {"蘋果": 20, "香蕉": 30, "橘子": 25}
d["蘋果"] = 10
print(d)
d["蓮霧"] = 15
print(d)

# 刪除字典的內容
# (delete dictionary content: remove items from the list)
d = {"蘋果": 20, "香蕉": 30, "橘子": 25}
d.pop("蘋果")  # 刪除蘋果 (remove apple)
# 如果要刪掉的key不存在，會出現KeyError，所以可以加上第二個參數，當key不存在時，不會有任何變化
# (If the key to be deleted does not exist, KeyError will occur, so you can add a second parameter,
# when the key does not exist, there will be no change)
popitem = d.pop("蓮霧", "不存在這筆資料")  # 不會有任何變化 (no change)
print(d)  # {'香蕉': 30, '橘子': 25}
print(popitem)  # 不存在這筆資料 (no such data)

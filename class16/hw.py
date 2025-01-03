
def add():
    global score_dict
    subject = input("請輸入想新增的科目:")
    if subject in score_dict:
        print("此科目已經新增過囉!")
    else:
        while True:
            try:
                score = int(input("請輸入分數:"))
                score_dict[subject] = score
                break
            except:
                print("輸入錯誤，請重新輸入")


def delete():
    global score_dict
    subject = input("請輸入想刪除的科目:")
    if subject in score_dict:
        score_dict.pop(subject)
        print("刪除成功!")
    else:
        print("此科目尚未新增!")


def exit():
    global score_dict
    if len(score_dict) == 0:
        print("目前沒有登記成績喔!")
    else:
        for subject, score in score_dict.items():
            print(f"{subject}:{score}")
        print(f"總平均為:{sum(score_dict.values())/len(score_dict)}")


score_dict = {}
while True:
    for subject, score in score_dict.items():
        print(f"{subject}:{score}")
    print("1. 新增科目成績")
    print("2. 刪除科目成績")
    print("3. 提交所有成績並顯示平均")
    choice = input("請輸入功能編號:")
    print("==========================")

    if choice == "1":
        add()
    elif choice == "2":
        delete()
    elif choice == "3":
        break
    else:
        print("查無此功能請重新輸入!")

    print("==========================")











訊息 python初階-週五-1900










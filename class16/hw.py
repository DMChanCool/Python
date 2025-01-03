def edit():
    global score_dict
    subject = input("請輸入想修改的科目:")
    if subject in score_dict:
        while True:
            try:
                score = int(input("請輸入新的分數:"))
                score_dict[subject] = score
                break
            except:
                print("輸入錯誤，請重新輸入")
    else:
        print("此科目尚未新增!")


score_dict = {}
functions = [add, delete, edit, exit]

while True:
    for subject, score in score_dict.items():
        print(f"{subject}:{score}")
    for i in range(len(functions)):  # function=指令名稱
        print(f"{i + 1}. {functions[i].__name__}")  # 顯示指令名稱當作選項
    try:
        choice = int(input("請輸入功能編號:"))
        print("==========================")

        if 1 <= choice < len(functions):
            functions[choice - 1]()  # add() or delete()
        elif choice == len(functions):
            functions[choice - 1]()  # exit()
            break
        else:
            print("無效的選擇，請重新輸入")

    except:
        print("輸入錯誤，請輸入數字")

    print("==========================")

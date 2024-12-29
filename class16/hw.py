"""
成績系統改寫作業 Score System Rewrite Assignment
--------------------------------------------

任務說明 (Task Description)：
請把成績系統的每個功能變成一個獨立的功能包，就像把工具分門別類放好一樣！
Please turn each feature of the score system into separate functions, just like organizing tools into different boxes!

需要製作的功能包 (Functions to Create)：
1. 新增功能 (Add Function):
   - def add: 幫我們加入新科目和分數
   - For adding new subject and score

2. 刪除功能 (Delete Function):
   - def delete: 可以刪掉不要的科目和分數
   - For removing subject and score

3. 離開功能 (Exit Function):
   - def exit: 結束程式並算出平均分數
   - For ending program and calculating average

完成方式 (How to Complete)：
- 要像積木一樣，把每個功能都組裝好
- Build each function like blocks
- 保持原本的操作方式不變
- Keep the same way of using the program
"""


def add(scores):
    """
    Add a new subject and its score.

    Args:
        scores (dict): The current score dictionary.

    Returns:
        dict: Updated score dictionary.
    """
    subject = input("請輸入科目名稱 (Enter subject name): ")
    if subject in scores:
        print(f"科目 {subject} 已存在 (Subject {subject} already exists).")
    else:
        try:
            score = float(input("請輸入分數 (Enter score): "))
            scores[subject] = score
            print(
                f"成功加入 {subject} 分數 {score} (Successfully added {subject} with score {score})."
            )
        except ValueError:
            print("分數無效，請輸入數字 (Invalid score, please enter a number).")
    return scores


def delete(scores):
    """
    Delete a subject and its score.

    Args:
        scores (dict): The current score dictionary.

    Returns:
        dict: Updated score dictionary.
    """
    subject = input("請輸入要刪除的科目名稱 (Enter subject name to delete): ")
    if subject in scores:
        del scores[subject]
        print(f"科目 {subject} 已刪除 (Subject {subject} deleted).")
    else:
        print(f"科目 {subject} 不存在 (Subject {subject} does not exist).")
    return scores


def exit_program(scores):
    """
    Exit the program and calculate the average score.

    Args:
        scores (dict): The current score dictionary.
    """
    if scores:
        average = sum(scores.values()) / len(scores)
        print(f"平均分數為: {average:.2f} (Average score: {average:.2f}).")
    else:
        print("沒有任何分數記錄 (No scores recorded).")
    print("程式結束 (Program ended). 再見 (Goodbye)!")
    return True


def main():
    """
    Main function to run the score system.
    """
    scores = {}
    while True:
        print("\n1. 新增 (Add)\n2. 刪除 (Delete)\n3. 離開 (Exit)")
        choice = input("請選擇操作 (Choose an option): ")
        if choice == "1":
            scores = add(scores)
        elif choice == "2":
            scores = delete(scores)
        elif choice == "3":
            if exit_program(scores):
                break
        else:
            print("無效選擇，請重新輸入 (Invalid choice, please try again).")


if __name__ == "__main__":
    main()

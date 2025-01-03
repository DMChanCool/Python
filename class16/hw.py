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

"""
**Function Menu**
1. Add a subject and its score  
2. Delete a subject's score  
3. Exit the system  

In every step, show the current scores and the function menu.

---

**Example Terminal Output**:

```plaintext
1. Add a subject and score
2. Delete a subject's score
3. Submit all scores and show the average
Please enter the function number: 1
==========================
Enter the subject you want to add: English
Enter the score: 100
==========================
English: 100
1. Add a subject and score
2. Delete a subject's score
3. Submit all scores and show the average
Please enter the function number: 1
==========================
Enter the subject you want to add: Chinese
Enter the score: aaaaa
Invalid input, please enter a number.
Enter the score: 2
==========================
English: 100
Chinese: 2
1. Add a subject and score
2. Delete a subject's score
3. Submit all scores and show the average
Please enter the function number: 1
==========================
Enter the subject you want to add: Math
Enter the score: 55
==========================
English: 100
Chinese: 2
Math: 55
1. Add a subject and score
2. Delete a subject's score
3. Submit all scores and show the average
Please enter the function number: 2
==========================
Enter the subject you want to delete: Science
This subject has not been added!
==========================
English: 100
Chinese: 2
Math: 55
1. Add a subject and score
2. Delete a subject's score
3. Submit all scores and show the average
Please enter the function number: 2
==========================
Enter the subject you want to delete: English
Successfully deleted!
==========================
Chinese: 2
Math: 55
1. Add a subject and score
2. Delete a subject's score
3. Submit all scores and show the average
Please enter the function number: 3
==========================
Chinese: 2
Math: 55
The average score is: 28.5
```
"""

score_dict = {}
while True:
    for subject, score in score_dict.items():
        print(f"{subject}: {score}")
    print("1. Add a subject and score")
    print("2. Delete a subject's score")
    print("3. Exit the system")
    choice = input("Please enter the function number: ")
    if choice == "1":
        subject = input("Enter the subject you want to add: ")
        if subject in score_dict:
            print("This subject has already been added!")
        else:
            while True:
                try:
                    score = int(input("Enter the score: "))
                    score_dict[subject] = score
                    break
                except:
                    print("Invalid input, please enter a number.")
    elif choice == "2":
        subject = input("Enter the subject you want to delete: ")
        if subject in score_dict:
            score_dict.pop(subject)
            print("Successfully deleted!")
        else:
            print("This subject has not been added!")
    elif choice == "3":
        if len(score_dict) == 0:
            print("There is no score to show!")
        else:
            for subject, score in score_dict.items():
                print(f"{subject}: {score}")
            print("The average score is:", sum(score_dict.values()) / len(score_dict))
        break
    else:
        print("Invalid input, please enter a number.")

    print("================================================")

# for else
# if for loop ends normally, then execute the else block
# for i in range(5):
#     print(i)
# else:
#     print("for loop ends normally")

# i = 0
# while i < 5:
#     print(i)
#     i += 1
# else:
#     print("while loop ends normally")


"""
Create a countdown timer (in seconds) using a for loop.
- The user can enter a number of seconds.
- When the countdown reaches 0, display "Time's up!"

Example(in terminal):
---
Please enter the number of seconds: 3  
3  
2  
1  
Time's up! 

---

This way, the program will count down and show each second on the screen until it reaches zero.
"""

# import time

# i = int(input("Please enter the number of seconds: "))
# if i > 0:
#     for a in range(i, 0, -1):
#         print(a)
#         time.sleep(1)
#     else:
#         print("time is up!")

# #loop continue
# #skip one iteration of the loop and continue with the next iteration
# for i in range(5):
#     if i == 3:
#         continue
#     print(i)

# i =0
# while i < 5:
#     if i == 1
#         i+=1
#         continue
#     print(i)
#     i+=1

"""
Please enter the number of times you want to jump rope.
The student is jumping rope, and when they reach multiples of 10 (like 10, 20, 30…), they take a break. Use `continue` to skip jumping when it is the 10th, 20th, 30th... time.

Example:
Please enter the number of times you want to jump rope: 15
Jump 1 time
Jump 2 times
Jump 3 times
Jump 4 times
Jump 5 times
Jump 6 times
Jump 7 times
Jump 8 times
Jump 9 times
Take a break
Jump 11 times
Jump 12 times
Jump 13 times
Jump 14 times
Jump 15 times
"""

i = int(input("Please enter the number jumps: "))
if i > 0:
    for a in range(1, i + 1):

        if a % 10 == 0:
            print("Take a break")
            continue
        else:
            print(f"Jump {a} times")


# loop break
# exit loop immediately
# but note that this break will only exit the loop that it belongs to
# so you need to determine which loop this break belongs to first
for i in range(5):
    for j in range(5):
        if j == 3:
            break
        print(j)
    if i == 3:
        break
    print(i)

i = 0
while i < 5:
    if i == 3:
        break
    print(i)
    i += 1

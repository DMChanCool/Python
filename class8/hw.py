"""
Enter a range of whole numbers, and the program will display all the prime numbers within that range.
(you can refer to the example in class for modification)

Example(in terminal):
---
Please enter the starting number: 10  
Please enter the ending number: 50  

Result:  
11  
13  
17  
19  
23  
29  
31  
37  
41  
43  
47  

---

In this example, the program finds and lists all prime numbers between 10 and 50.
"""

start = int(input("Please enter the starting number: "))
end = int(input("Please enter the ending number: "))

for i in range(start, end + 1):

    is_prime = True
    for i in range(2, i):
        if num % i == 0:
            is_prime = False

        if is_prime and num > 1:
            print(f"{num}is a prime number.")
        else:
            print(f"{num}is not a prime number.")

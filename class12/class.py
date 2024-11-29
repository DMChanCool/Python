# list 型態轉換(change something into a list- like magic)
print(range(10))  # create a range but we can't see the numbers
print(list(range(10)))  # change numbers into a list
print(list("hello"))  # change a word into a list

# split (cut a string into pieces)
s = "hello world"
L = s.split("")  # cut the string where there are spaces
print(L)
calendar = "2021/12/25"
L = calendar.split("/")  # cut the string where there are /
print(L)

# join
L = ["hello", "world"]
s = " ".join(L)  # put words together with spaces between them
print(s)

# append (add soemthing new at the end)
L = ["Hello", "World"]
L.append("Python")  # add 'python' to the end of the list
print(L)

# remove (take something out)
L = ["Hello", "World", "Python"]
L.remove("World")  # remove 'World' from the list
print(L)

# pop(take out and remember)
L = ["Hello", "World", "Python"]
s = L.pop(1)  # remove the second item from the list and remember it
print(s)

# count(how many are there)
L = ["Hello", "World", "Python", "Hello"]
print(L.count("Hello"))  # how many 'Hello' are there?

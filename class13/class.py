# index : find where something is in a list, just like finding a toy in your toy box!)
L = {1, 3, 2, 4, 5}
print(L.index(3))  # 1

# sort : put things in order from smallest to biggest, like arranging pencils by length
L = [1, 3, 2, 4, 5]
L.sort()
print(L)

# sort reverse : put things in order from biggest to smallest
L = [1, 3, 2, 4, 5]
L.sort(reverse=True)
print(L)

# reverse : put things in order from biggest to smallest, like arranging pencils by length
L = [1, 3, 2, 4, 5]
L.reverse()
print(L)

# dictionary : a special box where we can store things with names, like labeling boxes
# create dictionary: make a list of names and values
d = {"name": "dmchan", "age": 20, "gender": "male"}
print(d)

# get dictionary value: find out how many items we have for each thing
d = {"name": "dmchan", "age": 20, "gender": "male"}
print(d["name"])
print(d["age"])
print(d["gender"])

# len : find out how many items are in the dictionary
d = {"name": "dmchan", "age": 20, "gender": "male"}
print(len(d))

# check if key exists: see if we have a box for a certain toy
d = {"name": "dmchan", "age": 20, "gender": "male"}
print("name" in d)  # True
print("height" in d)  # False

# loop through dictionary: go through each item in the dictionary one by one
d = {"name": "dmchan", "age": 20, "gender": "male"}
for key in d:
    print(key)  # this prints only the key-the name we gave for each item
    print(d[key])  # this prints the value-the number we stored with the key

for k in d.keys:
    print(k)  # this prints only the key-like reading the labels on boxes
    print(d[k])  # this prints the value-like counting what's in the boxes

for v in d.values:
    print(v)  # this prints only the value-just the number we stored

for k, v in d.items():
    print(
        f"{k}:{v}"
    )  # this prints both the key and the value - like saying "dmchan is 20 years old"

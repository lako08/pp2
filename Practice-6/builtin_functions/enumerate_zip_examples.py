# enumerate
names = ["Alice", "Bob", "Charlie"]

for index, name in enumerate(names):
    print(index, name)

# zip
list1 = [1, 2, 3]
list2 = ["a", "b", "c"]

for num, letter in zip(list1, list2):
    print(num, letter)
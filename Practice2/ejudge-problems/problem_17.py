n = int(input())
count_dict = {}

for _ in range(n):
    number = input()
    count_dict[number] = count_dict.get(number, 0) + 1

result = 0
for count in count_dict.values():
    if count == 3:
        result += 1

print(result)
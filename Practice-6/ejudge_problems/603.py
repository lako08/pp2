n = int(input())
words = input().split()

result = [f"{index}:{word}" for index, word in enumerate(words)]
print(' '.join(result))
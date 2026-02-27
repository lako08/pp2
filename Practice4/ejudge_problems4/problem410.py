def cycle_generator(lst, k):
    for _ in range(k):
        for item in lst:
            yield item


lst = input().split() 
k = int(input())      

result = list(cycle_generator(lst, k))

print(*result)
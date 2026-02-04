n = int(input())
doramas = {}

for _ in range(n):
    s, k = input().split()
    k = int(k)
    doramas[s] = doramas.get(s, 0) + k

for name in sorted(doramas.keys()):
    print(name, doramas[name])
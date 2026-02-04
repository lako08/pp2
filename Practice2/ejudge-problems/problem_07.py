n=int(input())
s=input().split()
max_num=int(s[0])
p=1
for i in range(1, n):
    num=int(s[i])
    if max_num<num:
        max_num=num
        p=i+1
print(p)
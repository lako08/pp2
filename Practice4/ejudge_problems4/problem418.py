x1, y1 = map(float, input().strip().split())
x2, y2 = map(float, input().strip().split())

x2_reflected = x2
y2_reflected = -y2

if x1 == x2_reflected:
    x_reflection = x1
else:
    t = -y1 / (y2_reflected - y1)
    x_reflection = x1 + t * (x2_reflected - x1)

print(f"{x_reflection:.10f} 0.0000000000")
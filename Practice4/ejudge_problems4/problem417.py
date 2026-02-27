import math

R = float(input())
x1, y1 = map(float, input().split())
x2, y2 = map(float, input().split())

# Direction vector of the segment
dx = x2 - x1
dy = y2 - y1

# Quadratic coefficients: |P1 + t*(P2-P1)|^2 = R^2
a = dx*dx + dy*dy
b = 2*(x1*dx + y1*dy)
c = x1*x1 + y1*y1 - R*R

discriminant = b*b - 4*a*c

if discriminant < 0:
    # No intersection
    length = 0.0
else:
    sqrt_disc = math.sqrt(discriminant)
    t1 = (-b - sqrt_disc) / (2*a)
    t2 = (-b + sqrt_disc) / (2*a)
    
    # Clip t to [0,1]
    t_enter = max(0, min(t1, t2))
    t_exit = min(1, max(t1, t2))
    
    if t_enter > t_exit:
        length = 0.0
    else:
        length = math.hypot(dx, dy) * (t_exit - t_enter)

print(f"{length:.10f}")
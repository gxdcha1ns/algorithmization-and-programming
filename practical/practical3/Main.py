items = [10.05, 20.10, 30.20]
sum_items = sum(items)
check_total = 60.35
epsilon = 1e-10
is_valid = abs(sum_items - check_total) < epsilon
print(is_valid)

a, b, c = 3.0, 4.0, 5.0
p = (a + b + c) / 2
area = (p * (p - a) * (p - b) * (p - c))**0.5 if p * (p - a) * (p - b) * (p - c) >= 0 else 0
print(area)
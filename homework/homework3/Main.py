a, b, expected_c = 3.0, 4.0, 5.0
c = (a**2 + b**2)**0.5
perimeter = a + b + c
match = abs(c - expected_c) < 1e-6
print(f"Гіпотенуза: {c}, Периметр: {perimeter}, Збігається: {match}")
number = 245
d1 = number // 100
d2 = (number // 10) % 10
d3 = number % 10
sum_squares = d1**2 + d2**2 + d3**2
print(f"Сума квадратів цифр ({d1}^2 + {d2}^2 + {d3}^2): {sum_squares}")
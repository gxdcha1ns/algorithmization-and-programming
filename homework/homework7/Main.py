
n = int(input("Введіть N: "))
total = 0

for i in range(2, n + 1):
    is_prime = True

    for j in range(2, i):
        if i % j == 0:
            is_prime = False
            break

    if is_prime:
        total += i

print(f"Сума простих чисел від 2 до {n}: {total}")

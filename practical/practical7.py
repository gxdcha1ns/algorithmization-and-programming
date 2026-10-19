
n = int(input("Введіть розмір таблиці множення: "))

for i in range(1, n + 1):
    for j in range(1, n + 1):
        print(f"{i * j:4}", end="")
    print()

n = int(input("Введіть номер числа Фібоначчі: "))

a = 0
b = 1
i = 0

while i < n:
    a, b = b, a + b
    i += 1

print(f"{n}-е число Фібоначчі: {a}")

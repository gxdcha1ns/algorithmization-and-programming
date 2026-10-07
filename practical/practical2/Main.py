binary = '1011'
result = 0
for digit in binary:
    result = result * 2 + int(digit)
print(result)

number = 345
d1 = number // 100
d2 = (number // 10) % 10
d3 = number % 10
reversed_number = d3 * 100 + d2 * 10 + d1
print(reversed_number)
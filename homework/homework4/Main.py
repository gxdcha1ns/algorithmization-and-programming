number = 13
bit_3_set = (number & (1 << 3)) != 0
multiplied = number << 3
print(f"3-й біт увімкнений: {bit_3_set}, Число * 8: {multiplied}")
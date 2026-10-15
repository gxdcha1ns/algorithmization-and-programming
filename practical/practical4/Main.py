READ = 1 << 0
WRITE = 1 << 1
EXECUTE = 1 << 2
user_permissions = READ | EXECUTE
can_write = (user_permissions & WRITE) != 0
print(can_write)

n = 29
parity = "парне" if (n & 1) == 0 else "непарне"
power_of_two = (n & (n - 1)) == 0 and n != 0
bits_set = bin(n).count('1')
lowest_bit = n & -n
print(parity, power_of_two, bits_set, lowest_bit)
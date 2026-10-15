lst = [5, 3, 9, 1, 6]
total = 0
minimum = lst[0]
maximum = lst[0]
count = 0
for num in lst:
    total += num
    if num < minimum:
        minimum = num
    if num > maximum:
        maximum = num
    count += 1
print(total, minimum, maximum, count)

lst = [1, 2, 3, 4, 5]
i, j = 0, len(lst) - 1
while i < j:
    lst[i], lst[j] = lst[j], lst[i]
    i += 1
    j -= 1
print(lst)
def missing_number(items: list[int]) -> int:
    items.sort()
    for i in range(len(items) - 2):
        first, second, third = items[i: i + 3]
        if second - first != third - second:
            return third - (second - first)


print("Example:")
print(missing_number([1, 4, 2, 5]))

# These "asserts" are used for self-checking
assert missing_number([1, 2, 4, 5]) == 3
assert missing_number([2, 6, 8]) == 4

print("The mission is done! Click 'Check Solution' to earn rewards!")

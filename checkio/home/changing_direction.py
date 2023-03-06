def changing_direction(elements: list[int]) -> int:

    count_changed_directions = 0
    sequence = None
    for index in range(len(elements) - 1):
        if elements[index] == elements[index + 1]:
            continue
        sequence_is_asc = elements[index] < elements[index + 1]
        if sequence != sequence_is_asc:
            count_changed_directions += 1 if sequence is not None else 0
            sequence = sequence_is_asc

    return count_changed_directions


print("Example:")
print(changing_direction([1, 2, 2, 1, 2, 2]))

# These "asserts" are used for self-checking
assert changing_direction([1, 2, 3, 4, 5]) == 0
assert changing_direction([1, 2, 3, 2, 1]) == 1
assert changing_direction([1, 2, 2, 1, 2, 2]) == 2

print("The mission is done! Click 'Check Solution' to earn rewards!")

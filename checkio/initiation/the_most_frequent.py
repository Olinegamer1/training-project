import timeit, random, string


def most_frequent(data: list[str]) -> str:
    return max(data, key=data.count)
    dictionary = dict()
    for symbol in data:
        if symbol not in dictionary:
            dictionary.setdefault(symbol, 1)
        dictionary[symbol] = dictionary.get(symbol) + 1
    return key_with_max_value(dictionary)


def key_with_max_value(dictionary):
    values = list(dictionary.values())
    keys = list(dictionary.keys())
    return keys[values.index(max(values))]


print("Example:")
print(most_frequent(["a", "b", "c", "a", "b", "a"]))

# These "asserts" are used for self-checking
assert most_frequent(["a", "b", "c", "a", "b", "a"]) == "a"
assert most_frequent(["a", "a", "bi", "bi", "bi"]) == "bi"

print("The mission is done! Click 'Check Solution' to earn rewards!")

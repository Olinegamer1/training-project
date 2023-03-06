def second_index(text: str, symbol: str) -> [int, None]:
    if text.count(symbol) < 2:
        return None
    first = text.find(symbol)
    return text.find(symbol, first + 1)



print("Example:")
print(second_index("find the river", "e"))

assert second_index("sims", "s") == 3
assert second_index("find the river", "e") == 12
assert second_index("hi", " ") == None
assert second_index("hi mayor", " ") == None
assert second_index("hi mr Mayor", " ") == 5

print("The mission is done! Click 'Check Solution' to earn rewards!")

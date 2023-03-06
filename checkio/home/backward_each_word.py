def backward_string_by_word(text: str) -> str:
    return ' '.join(x[::-1] for x in text.split(' '))


# print("Example:")
print(backward_string_by_word("hello   world"))

# # These "asserts" are used for self-checking
# assert backward_string_by_word("") == ""
# assert backward_string_by_word("world") == "dlrow"
# assert backward_string_by_word("hello world") == "olleh dlrow"
# assert backward_string_by_word("hello   world") == "olleh   dlrow"
# assert backward_string_by_word("welcome to a game") == "emoclew ot a emag"
#
# print("The mission is done! Click 'Check Solution' to earn rewards!")

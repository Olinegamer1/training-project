def safe_pawns(pawns: set) -> int:
    safe_pawns_count = 0
    for pawn in pawns:
        char, digit = map(ord, pawn)
        for safe_pawn in [chr(char - 1) + chr(digit - 1), chr(char + 1) + chr(digit - 1)]:
            if safe_pawn in pawns:
                safe_pawns_count += 1
                break

    return safe_pawns_count


print("Example:")
print(safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}))

assert safe_pawns({"d2", "f4", "d4", "b4", "e3", "g5", "c3"}) == 6
assert safe_pawns({"f4", "g4", "d4", "b4", "e4", "e5", "c4"}) == 1

print("The mission is done! Click 'Check Solution' to earn rewards!")

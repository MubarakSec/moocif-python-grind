# The most common character in a string
def most_common_character(s: str) -> str:
    # Count occurrences of each character
    counts = {}
    for ch in s:
        counts[ch] = counts.get(ch, 0) + 1

    # Find the character with the highest count, breaking ties by first appearance
    best_char = None
    best_count = -1
    for ch in s:
        cnt = counts[ch]
        if cnt > best_count:
            best_count = cnt
            best_char = ch

    return best_char


# Example usage:
if __name__ == "__main__":
    first_string = "abcdbde"
    print(most_common_character(first_string))      # Output: b

    second_string = "exemplaryelementary"
    print(most_common_character(second_string))     # Output: e


if __name__ == "__main__":
    first_string = "abcdbde"
    print(most_common_character(first_string))

    second_string = "exemplaryelementary"
    print(most_common_character(second_string))

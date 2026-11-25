"""Validation: range, length, presence and type checks

Notes, live tools and self-marking practice:
https://revisionhub.online/igcse-computer-science-0478/algorithm-design-and-problem-solving/

Part of Revision Hub CS code examples - https://revisionhub.online
"""

def range_check(value, low, high):
    return low <= value <= high


def length_check(text, min_len, max_len):
    return min_len <= len(text) <= max_len


def presence_check(text):
    return text.strip() != ""


def type_check_integer(text):
    return text.strip().lstrip("-").isdigit()


def get_mark():
    """Keep asking until a whole number from 0 to 100 is entered."""
    entry = input("Enter a mark (0-100): ")
    while not (type_check_integer(entry) and range_check(int(entry), 0, 100)):
        entry = input("Invalid. Enter a whole number from 0 to 100: ")
    return int(entry)


if __name__ == "__main__":
    print(range_check(101, 0, 100))      # False
    print(length_check("abc123", 6, 12)) # True
    print(presence_check("   "))         # False
    print(type_check_integer("42"))      # True

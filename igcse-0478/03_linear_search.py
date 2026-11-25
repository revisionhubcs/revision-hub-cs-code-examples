"""Linear search

Notes, live tools and self-marking practice:
https://revisionhub.online/igcse-computer-science-0478/algorithm-design-and-problem-solving/

Part of Revision Hub CS code examples - https://revisionhub.online
"""

def linear_search(items, target):
    """Return the 1-based position of target, or 0 if not found."""
    position = 0
    index = 0
    while index < len(items) and position == 0:
        if items[index] == target:
            position = index + 1
        index = index + 1
    return position


if __name__ == "__main__":
    names = ["Ali", "Ben", "Cara", "Dev"]
    found = linear_search(names, "Cara")
    print("Found at position", found if found else "Not found")   # 3
    print(linear_search(names, "Zoe"))                              # 0

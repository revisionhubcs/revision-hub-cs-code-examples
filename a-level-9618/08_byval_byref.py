"""Passing parameters by value and by reference

Notes, live tools and self-marking practice:
https://revisionhub.online/a-level-computer-science-9618/programming-9618/

Part of Revision Hub CS code examples - https://revisionhub.online
"""

def add_one_by_value(x):
    x = x + 1                        # changes only the local copy
    return x


def add_one_to_list(values):
    values[0] = values[0] + 1        # lists are mutable: the original changes (like BYREF)


if __name__ == "__main__":
    n = 5
    add_one_by_value(n)
    print(n)                         # 5  (unchanged)
    box = [5]
    add_one_to_list(box)
    print(box[0])                    # 6  (changed)

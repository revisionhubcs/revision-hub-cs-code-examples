"""Procedures, functions and parameters

Notes, live tools and self-marking practice:
https://revisionhub.online/igcse-computer-science-0478/programming/

Part of Revision Hub CS code examples - https://revisionhub.online
"""

def show_line(length):
    """A procedure: performs a task and returns nothing."""
    print("-" * length)


def area_of_rectangle(width, height):
    """A function: always returns a value."""
    return width * height


if __name__ == "__main__":
    show_line(10)
    print(area_of_rectangle(4, 5))   # 20

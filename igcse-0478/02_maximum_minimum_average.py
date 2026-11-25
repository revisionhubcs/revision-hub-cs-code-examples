"""Maximum, minimum and average

Notes, live tools and self-marking practice:
https://revisionhub.online/igcse-computer-science-0478/algorithm-design-and-problem-solving/

Part of Revision Hub CS code examples - https://revisionhub.online
"""

def max_min_average(marks):
    """Return the highest, lowest and mean of a non-empty list."""
    highest = marks[0]
    lowest = marks[0]
    total = 0
    for mark in marks:
        if mark > highest:
            highest = mark
        if mark < lowest:
            lowest = mark
        total = total + mark
    average = total / len(marks)    # calculated AFTER the loop
    return highest, lowest, average


if __name__ == "__main__":
    print(max_min_average([56, 78, 43, 91, 67]))   # (91, 43, 67.0)

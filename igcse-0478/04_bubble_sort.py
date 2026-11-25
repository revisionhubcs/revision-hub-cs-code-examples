"""Bubble sort

Notes, live tools and self-marking practice:
https://revisionhub.online/igcse-computer-science-0478/algorithm-design-and-problem-solving/

Part of Revision Hub CS code examples - https://revisionhub.online
"""

def bubble_sort(items):
    """Sort a list into ascending order using bubble sort (returns a new list)."""
    data = list(items)
    swapped = True
    passes = len(data) - 1
    while swapped and passes > 0:
        swapped = False
        for i in range(passes):
            if data[i] > data[i + 1]:
                data[i], data[i + 1] = data[i + 1], data[i]
                swapped = True
        passes = passes - 1
    return data


if __name__ == "__main__":
    print(bubble_sort([5, 9, 2, 7]))   # [2, 5, 7, 9]

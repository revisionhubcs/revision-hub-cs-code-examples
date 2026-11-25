"""Insertion sort

Notes, live tools and self-marking practice:
https://revisionhub.online/a-level-computer-science-9618/algorithm-design-9618/

Part of Revision Hub CS code examples - https://revisionhub.online
"""

def insertion_sort(items):
    data = list(items)
    for i in range(1, len(data)):
        key = data[i]
        j = i - 1
        while j >= 0 and data[j] > key:
            data[j + 1] = data[j]
            j = j - 1
        data[j + 1] = key
    return data


if __name__ == "__main__":
    print(insertion_sort([19, 3, 25, 8, 12]))   # [3, 8, 12, 19, 25]

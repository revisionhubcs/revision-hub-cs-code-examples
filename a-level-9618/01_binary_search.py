"""Binary search

Notes, live tools and self-marking practice:
https://revisionhub.online/a-level-computer-science-9618/algorithm-design-9618/

Part of Revision Hub CS code examples - https://revisionhub.online
"""

def binary_search(items, target):
    """Return the 0-based index of target in a sorted list, or -1."""
    low, high = 0, len(items) - 1
    while low <= high:
        mid = (low + high) // 2
        if items[mid] == target:
            return mid
        if items[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1


if __name__ == "__main__":
    data = [3, 8, 12, 19, 25, 31, 40]
    print(binary_search(data, 25))   # 4
    print(binary_search(data, 7))    # -1

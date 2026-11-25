"""Recursion: factorial and binary search

Notes, live tools and self-marking practice:
https://revisionhub.online/a-level-computer-science-9618/computational-thinking-problem-solving/

Part of Revision Hub CS code examples - https://revisionhub.online
"""

def factorial(n):
    if n <= 1:                       # base case
        return 1
    return n * factorial(n - 1)      # recursive call


def recursive_binary_search(items, target, low, high):
    if low > high:
        return -1
    mid = (low + high) // 2
    if items[mid] == target:
        return mid
    if items[mid] < target:
        return recursive_binary_search(items, target, mid + 1, high)
    return recursive_binary_search(items, target, low, mid - 1)


if __name__ == "__main__":
    print(factorial(5))                                         # 120
    data = [2, 5, 9, 14, 21]
    print(recursive_binary_search(data, 14, 0, len(data) - 1))  # 3

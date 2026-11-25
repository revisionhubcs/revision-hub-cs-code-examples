"""Totalling and counting

Notes, live tools and self-marking practice:
https://revisionhub.online/igcse-computer-science-0478/algorithm-design-and-problem-solving/

Part of Revision Hub CS code examples - https://revisionhub.online
"""

def total_and_count(numbers, limit):
    """Return the total of all numbers and how many are above limit."""
    total = 0
    count = 0
    for num in numbers:
        total = total + num
        if num > limit:
            count = count + 1
    return total, count


if __name__ == "__main__":
    data = [4, 12, 15, 8, 20]
    total, count = total_and_count(data, 10)
    print("Total:", total)            # 59
    print("Above 10:", count)         # 3

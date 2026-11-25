"""Stack (LIFO) using an array

Notes, live tools and self-marking practice:
https://revisionhub.online/a-level-computer-science-9618/data-types-and-structures/

Part of Revision Hub CS code examples - https://revisionhub.online
"""

class Stack:
    def __init__(self, size):
        self.items = [None] * size
        self.top = -1                # -1 means empty

    def push(self, item):
        if self.top == len(self.items) - 1:
            return False             # stack full
        self.top += 1
        self.items[self.top] = item
        return True

    def pop(self):
        if self.top == -1:
            return None              # stack empty
        item = self.items[self.top]
        self.top -= 1
        return item


if __name__ == "__main__":
    s = Stack(3)
    for x in ["A", "B", "C", "D"]:
        print("push", x, s.push(x))  # D fails: stack full
    print(s.pop(), s.pop())          # C B

"""Circular queue (FIFO)

Notes, live tools and self-marking practice:
https://revisionhub.online/a-level-computer-science-9618/data-types-and-structures/

Part of Revision Hub CS code examples - https://revisionhub.online
"""

class CircularQueue:
    def __init__(self, size):
        self.items = [None] * size
        self.front = 0
        self.rear = -1
        self.count = 0

    def enqueue(self, item):
        if self.count == len(self.items):
            return False             # queue full
        self.rear = (self.rear + 1) % len(self.items)
        self.items[self.rear] = item
        self.count += 1
        return True

    def dequeue(self):
        if self.count == 0:
            return None              # queue empty
        item = self.items[self.front]
        self.front = (self.front + 1) % len(self.items)
        self.count -= 1
        return item


if __name__ == "__main__":
    q = CircularQueue(3)
    for x in [1, 2, 3]:
        q.enqueue(x)
    print(q.dequeue(), q.enqueue(4), q.dequeue(), q.dequeue(), q.dequeue())  # 1 True 2 3 4

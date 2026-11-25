"""Linked list with a free list (array based)

Notes, live tools and self-marking practice:
https://revisionhub.online/a-level-computer-science-9618/data-types-and-structures/

Part of Revision Hub CS code examples - https://revisionhub.online
"""

NULL = -1


class LinkedList:
    def __init__(self, size):
        self.data = [None] * size
        self.pointer = list(range(1, size)) + [NULL]
        self.start = NULL
        self.free = 0

    def insert_ordered(self, item):
        if self.free == NULL:
            return False             # no free nodes
        new = self.free
        self.free = self.pointer[new]
        self.data[new] = item
        prev, cur = NULL, self.start
        while cur != NULL and self.data[cur] < item:
            prev, cur = cur, self.pointer[cur]
        self.pointer[new] = cur
        if prev == NULL:
            self.start = new
        else:
            self.pointer[prev] = new
        return True

    def to_list(self):
        out, cur = [], self.start
        while cur != NULL:
            out.append(self.data[cur])
            cur = self.pointer[cur]
        return out


if __name__ == "__main__":
    ll = LinkedList(5)
    for x in [30, 10, 20]:
        ll.insert_ordered(x)
    print(ll.to_list())              # [10, 20, 30]

"""DIV, MOD, ROUND and RANDOM

Notes, live tools and self-marking practice:
https://revisionhub.online/igcse-computer-science-0478/programming/

Part of Revision Hub CS code examples - https://revisionhub.online
"""

import random


def div_mod(a, b):
    return a // b, a % b             # DIV and MOD


def dice():
    """Random whole number from 1 to 6."""
    return random.randint(1, 6)


if __name__ == "__main__":
    print(div_mod(17, 5))            # (3, 2)
    print(round(7.456, 1))           # 7.5
    print(dice())

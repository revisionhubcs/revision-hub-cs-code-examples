"""Binary, denary and hexadecimal conversion

Notes, live tools and self-marking practice:
https://revisionhub.online/igcse-computer-science-0478/data-representation/

Part of Revision Hub CS code examples - https://revisionhub.online
"""

def denary_to_binary(n, bits=8):
    result = ""
    for _ in range(bits):
        result = str(n % 2) + result
        n = n // 2
    return result


def binary_to_denary(b):
    total = 0
    for bit in b:
        total = total * 2 + int(bit)
    return total


def binary_to_hex(b):
    digits = "0123456789ABCDEF"
    b = b.zfill((len(b) + 3) // 4 * 4)
    return "".join(digits[binary_to_denary(b[i:i + 4])] for i in range(0, len(b), 4))


if __name__ == "__main__":
    print(denary_to_binary(87))          # 01010111
    print(binary_to_denary("10110101"))  # 181
    print(binary_to_hex("11101011"))     # EB

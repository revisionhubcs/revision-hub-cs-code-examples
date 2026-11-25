"""File handling: write and read a text file

Notes, live tools and self-marking practice:
https://revisionhub.online/igcse-computer-science-0478/programming/

Part of Revision Hub CS code examples - https://revisionhub.online
"""

def write_names(filename, names):
    with open(filename, "w") as f:
        for name in names:
            f.write(name + "\n")


def read_names(filename):
    with open(filename) as f:
        return [line.strip() for line in f]


if __name__ == "__main__":
    write_names("names.txt", ["Ali", "Ben", "Cara"])
    print(read_names("names.txt"))   # ['Ali', 'Ben', 'Cara']

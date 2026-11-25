"""String handling

Notes, live tools and self-marking practice:
https://revisionhub.online/igcse-computer-science-0478/programming/

Part of Revision Hub CS code examples - https://revisionhub.online
"""

def string_demo(word):
    return {
        "length": len(word),             # LENGTH
        "substring": word[3:6],          # SUBSTRING(word, 4, 3)
        "upper": word.upper(),           # UCASE
        "lower": word.lower(),           # LCASE
    }


if __name__ == "__main__":
    print(string_demo("Computer"))
    # {'length': 8, 'substring': 'put', 'upper': 'COMPUTER', 'lower': 'computer'}

'''
1.1
Is Unique: Implement an algorithm to determine if a string has all unique characters. What if you cannot use additional data structures?
Hints: #44, #117, #132
'''

from sys import argv

# With data structures allowed

def is_unique(the_str: str) -> bool:
    chars = dict()
    for c in the_str:
        if c in chars:
            return False
        chars[c] = c
    return True


if __name__ == "__main__":
    input_strings = argv[1]
    for s in input_strings.split(','):
        print(f"{s}: {is_unique(s)}")


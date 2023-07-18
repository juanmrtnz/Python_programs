import re
import sys


def main():
    print(count(input("Text: ").strip()))


def count(s):
    matches = re.findall(r"(?:(?:\W+?)(um[.,\?]+?)|^(um[.,\?]+?)|^um$)", s, re.IGNORECASE)
    return len(matches)


if __name__ == "__main__":
    main()
import re
import sys


def main():
    print(validate(input("IPv4 Address: ").strip()))


def validate(ip):
    try:
        match = re.search(r"^(\d+)\.(\d+)\.(\d+)\.(\d+)$", ip)
        for _ in range(1, 5):
            if 0 <= int(match.group(_)) <= 255:
                pass
            else:
                return False
        return True
    except (ValueError, AttributeError):
        return False


if __name__ == "__main__":
    main()

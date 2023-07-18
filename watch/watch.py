import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    if match := re.search(r'^<iframe(?: width="560" height="315")? src="(https?://(?:www\.)?youtube\.com/embed/.+)"(?: title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen)?></iframe>$', s, re.IGNORECASE):
        return re.sub(r'https?://(?:www\.)?youtube\.com/embed', 'https://youtu.be', match.group(1))
    else:
        return None


if __name__ == '__main__':
    main()
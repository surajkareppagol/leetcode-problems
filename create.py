from os import mkdir
from sys import argv


def main(path):
    mkdir(path.replace(" ", "-"))


if __name__ == "__main__":
    main(argv[1])

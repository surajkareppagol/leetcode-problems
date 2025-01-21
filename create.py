from os import chdir, mkdir
from sys import argv


def main(path):
    path = path.replace(".", "")
    path = path.replace(" ", "-")

    mkdir(path)

    code = """from typing import List

inputs = {1: [], 2: []}

for _, input in inputs.items():
    print("---> Solution ", _)
    print(Solution().function(*input))
    print()
"""

    markdown = "# 🧩"

    chdir(path)

    with open("main.py", "w") as file:
        file.write(code)

    with open("README.md", "w") as file:
        file.write(markdown)


if __name__ == "__main__":
    main(argv[1])

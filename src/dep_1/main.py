import sys

import dep_2


def main():
    print("Hello from dep_1.")
    dep_2.main()


if __name__ == "__main__":
    sys.exit(main())

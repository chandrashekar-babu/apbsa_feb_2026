a = 12345
testdata = "This is a test string"
b = [11, 22, 33, 44]

import time

def testfn():
    c = "Local variable in testfn"
    d = [1, 2, 3, 4]
    print(f"{locals()=}")
    print("-" * 30)

    print(f"{globals()=}")
    print("-" * 30)

    print(f"{vars()=}")

    print(f"'a' in vars(): {"a" in vars()}")  # Check if 'a' is in the current local scope
    print(f"'c' in vars(): {"c" in vars()}")  # Check if 'c' is in the current local scope (it should not be, since it's local to testfn)


if __name__ == "__main__":
    testfn()
    print("=" * 30)
    print(f"In main: {globals()=}")
    print("-" * 30)
    print(f"In main: {locals()=}")
    print("-" * 30)
    print(f"In main: {vars()=}")

    print(f"'a' in vars(): {"a" in vars()}")  # Check if 'a' is in the current local scope
    print(f"'c' in vars(): {"c" in vars()}")  # Check if 'c' is in the current local scope (it should not be, since it's local to testfn)
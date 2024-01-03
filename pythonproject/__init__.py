from sys import argv


def caller(func):
    def wrapped_func():
        print("first caller")
        print("Ans: ", func(argv[1], argv[2]))

    return wrapped_func


def main(func):
    def wrapped_func():
        print("second caller")
        print("Ans: ", func(argv[1], argv[2]))

    return wrapped_func


@caller
@main
def counter(str1: str, str2: str) -> int:
    print("func call")
    str1, str2 = str1.lower(), str2.lower()
    count = 0
    for char in str1:
        if char in str2:
            count += str1.count(char)
    return count

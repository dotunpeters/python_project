from sys import argv


def main_deco(func):
    def wrapper():
        print("before...")
        func(argv[1])
        print("after...")

    return wrapper


@main_deco
def encdec(str_val: str) -> None:
    """Encode - Decode string"""
    str_val.encode("ascii")
    print("encoded string:", str_val)
    # str_val.decode("ascii")
    # print("decoded string:", str_val)

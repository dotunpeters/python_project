def length(str_val: str) -> int:
    if str_val == "":
        return 0
    return 1 + length(str_val[1:])


def main():
    print(length("DotunPeter"))


if __name__ == "__main__":
    main()

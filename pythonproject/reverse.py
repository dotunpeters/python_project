def reverse(str_val: str) -> str:
    print(str_val)
    if len(str_val) == 0:
        return str_val
    return str_val[-1] + reverse(str_val[:-1])


def main():
    print(reverse("Dotun"))


if __name__ == "__main__":
    main()

def main(str1: str, str2: str) -> int:
    str1, str2 = str1.lower(), str2.lower()
    counter = 0
    for char in str1:
        if char in str2:
            counter += str1.count(char)
    return counter


if __name__ == "__main__":
    main("hello world", "hi people")

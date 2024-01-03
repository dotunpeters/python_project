from sys import argv


def reverse_recursion(str_val: str) -> str:
    if len(str_val) == 0:
        return str_val
    else:
        return reverse_recursion(str_val[1:]) + str_val[0]


def main():
    result = reverse_recursion(argv[1])
    print("result: ", result)

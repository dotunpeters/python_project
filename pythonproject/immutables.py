from functools import reduce


def main():
    my_list = [1, 2, 3, 4, 5]
    print(reduce(lambda x, y: x + y, my_list))
    print(sum(my_list))
    setattr(my_list, "name", "my_list")
    print(my_list.name)

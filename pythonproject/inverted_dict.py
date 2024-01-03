def inverted_dict(data: dict) -> dict:
    meanings = [x for x in data.values()]
    words = [y for y in data.keys()]

    new_dict = dict()
    for index in range(len(meanings)):
        if meanings[index] in new_dict.keys():
            new_dict[meanings[index]].append(words[index])
        else:
            new_dict[meanings[index]] = [words[index]]
    return new_dict


def main():
    d = inverted_dict(
        {
            "dubious": "doubtful",
            "hilarious": "amusing",
            "suspicious": "doubtful",
            "comical": "amusing",
            "hello": "hi",
        }
    )
    print(d)

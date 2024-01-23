class FlatIterator:
    def __init__(self, list_of_lists):
        self._flat_list = self.flatten_list(list_of_lists)
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._index < len(self._flat_list):
            item = self._flat_list[self._index]
            self._index += 1
            return item
        else:
            raise StopIteration

    def flatten_list(self, nested_list):
        result = []
        for item in nested_list:
            if isinstance(item, list):
                result.extend(self.flatten_list(item))
            else:
                result.append(item)
        return result


# test
ff = FlatIterator(
    [
        [["a"], ["b", "c"]],
        ["d", "e", [["f"], "h"], False],
        [1, 2, None, [[[[["!"]]]]], []],
    ]
)
for item in ff:
    print(item)


def test_3():
    list_of_lists_2 = [
        [["a"], ["b", "c"]],
        ["d", "e", [["f"], "h"], False],
        [1, 2, None, [[[[["!"]]]]], []],
    ]

    for flat_iterator_item, check_item in zip(
        FlatIterator(list_of_lists_2),
        ["a", "b", "c", "d", "e", "f", "h", False, 1, 2, None, "!"],
    ):
        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_2)) == [
        "a",
        "b",
        "c",
        "d",
        "e",
        "f",
        "h",
        False,
        1,
        2,
        None,
        "!",
    ]


if __name__ == "__main__":
    test_3()

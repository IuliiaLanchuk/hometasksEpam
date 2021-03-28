from task_find_occurrences.find_occurrences import find_occurrences

example_tree = {
    "first": ["RED", "BLUE", 2, ["a", 2, [6, ["list_in_lists"]]], ["m", True]],
    "second": {
        "simple_key": ["aa", [2], "',',", True, "'RED'a", "valued"],
    },
    "third": {
        "abc": ("BLUE", 7),
        "jhl": "RED",
        "some": {"nested_key": "RED"},
        "complex_key": {
            "key1": "value1",
            "key2": "RED",
            "key3": [
                ",",
                2,
                "of",
                "values",
                {"nested_key": "RED", "key7": ("BLUE", 7)},
            ],
        },
    },
    "fourth": 2,
    "any": {"nested_key": "RED"},
}


def test_find_occurrences_of_str():
    assert find_occurrences(example_tree, "RED") == 6


def test_find_occurrences_of_int():
    assert find_occurrences(example_tree, 2) == 5


def test_find_occurrences_of_list():
    assert find_occurrences(example_tree, [2]) == 1


def test_find_occurrences_of_list_in_lists():
    assert find_occurrences(example_tree, ["a", 2, [6, ["list_in_lists"]]]) == 1


def test_find_occurrences_of_tuple():
    assert find_occurrences(example_tree, ("BLUE", 7)) == 2


def test_find_occurrences_of_dict():
    assert find_occurrences(example_tree, {"nested_key": "RED"}) == 2


def test_find_occurrences_of_bool():
    assert find_occurrences(example_tree, True) == 2


def test_find_occurrences_in_empty_list():
    assert find_occurrences({}, "a") == 0


def test_find_occurrences_no_element():
    assert find_occurrences(example_tree, "") == 0

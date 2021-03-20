from project_filter.filter import Filter, make_filter


def test_apply_positive_even():
    positive_even = Filter(
        lambda a: a % 2 == 0, lambda a: a > 0, lambda a: isinstance(a, int)
    )
    assert positive_even.apply(range(10)) == [2, 4, 6, 8]


def test_apply_sum_with_7_is_zero():
    sum_with_7_is_zero = Filter(lambda a: a + 7 == 0)
    assert sum_with_7_is_zero.apply([-7, 13, 6.8, 9, 0]) == [-7]


def test_filter_of_empty_list_returns_empty_list():
    assert Filter().apply([]) == []


def test_empty_filter_returns_all_items():
    assert Filter().apply(range(5)) == [0, 1, 2, 3, 4]


def test_one_key_value_pair_repeats_in_different_team_members():
    team = [
        {
            "name": "Iuliia",
            "last_name": "Lanchuk",
            "hobby": "swimming",
            "type": "human",
        },
        {
            "name": "Barsik",
            "color": "black",
            "occupation": "was here",
            "type": "cat",
        },
        {
            "name": "Evgenii",
            "last_name": "Mukhailov",
            "hobby": "swimming",
            "type": "human",
        },
    ]
    assert make_filter(**{"type": "human"}).apply(team) == [
        {
            "name": "Iuliia",
            "last_name": "Lanchuk",
            "hobby": "swimming",
            "type": "human",
        },
        {
            "name": "Evgenii",
            "last_name": "Mukhailov",
            "hobby": "swimming",
            "type": "human",
        },
    ]


def test_no_such_key():
    team = [
        {
            "name": "Iuliia",
            "last_name": "Lanchuk",
            "hobby": "swimming",
            "type": "human",
        },
        {
            "name": "Barsik",
            "color": "black",
            "occupation": "was here",
            "type": "cat",
        },
        {
            "name": "Evgenii",
            "last_name": "Mukhailov",
            "hobby": "swimming",
            "type": "human",
        },
    ]
    assert make_filter(**{"hi": "human"}).apply(team) == []


def test_no_such_value():
    team = [
        {
            "name": "Iuliia",
            "last_name": "Lanchuk",
            "hobby": "swimming",
            "type": "human",
        },
        {
            "name": "Barsik",
            "color": "black",
            "occupation": "was here",
            "type": "cat",
        },
        {
            "name": "Evgenii",
            "last_name": "Mukhailov",
            "hobby": "swimming",
            "type": "human",
        },
    ]
    assert make_filter(**{"hobby": "dancing"}).apply(team) == []


def test_two_key_value_pairs_from_different_team_members():
    team = [
        {
            "name": "Iuliia",
            "last_name": "Lanchuk",
            "hobby": "swimming",
            "type": "human",
        },
        {
            "name": "Barsik",
            "color": "black",
            "occupation": "was here",
            "type": "cat",
        },
        {
            "name": "Evgenii",
            "last_name": "Mukhailov",
            "hobby": "swimming",
            "type": "human",
        },
    ]
    assert make_filter(**{"name": "Iuliia", "last_name": "Mukhailov"}).apply(team) == []

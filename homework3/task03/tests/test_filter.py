from typing import Any, Dict, List

import pytest
from project_filter.filter import Filter, make_filter

sample_data = [
    {
        "name": "Bill",
        "last_name": "Gilbert",
        "occupation": "was here",
        "type": "person",
    },
    {
        "is_dead": True,
        "kind": "parrot",
        "type": "bird",
        "name": "polly",
    },
]


@pytest.mark.parametrize(
    ("data", "expected_result"),
    [
        ({"name": "polly"}, [sample_data[1]]),
        ({"name": "Bill", "occupation": "was here"}, [sample_data[0]]),
        ({"name": "Iuliia"}, []),
    ],
)
def test_make_filter(data: Dict[Any, Any], expected_result: List[Any]):
    assert make_filter(**data).apply(sample_data) == expected_result


def test_apply():
    positive_even = Filter(
        lambda a: a % 2 == 0, lambda a: a > 0, lambda a: isinstance(a, int)
    )
    assert positive_even.apply(range(10)) == [2, 4, 6, 8]
    assert positive_even.apply(range(10)) != [0, 2, 4, 6]

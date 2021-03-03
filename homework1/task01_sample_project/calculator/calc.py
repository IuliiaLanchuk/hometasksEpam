"""
Task01.

1. please create your own git repository on github.
2. setup pre-commit hook with `black` and `isort` formatting for the repo
3. initialize .gitignore in the repository root sample)
4. create a `homework1` directory in the repo
5. then copy the `sample_project` into the directory.
6. fix all bugs in the `sample_project` code
7. write an extra test for each found bug

**Note**: as we said, any hw, which does not pass `isort --profile black --check` and `black --check`, will be rejected
"""


def check_power_of_2(a: int) -> bool:
    """
    I'm check is value a power of two.

    :param a: input value
    :return: bool
    """
    return type(a) == int and a != 0 and not (bool(a & (a - 1)))

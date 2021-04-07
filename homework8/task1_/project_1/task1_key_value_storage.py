"""We have a file that works as key-value storage, each like is represented as key and value separated by = symbol.

example:

name=kek
last_name=top
song_name=shadilay
power=9001

Values can be strings or integer numbers.
If a value can be treated both as a number and a string, it is treated as number.

Write a wrapper class for this key value storage that works like this:

storage = KeyValueStorage('path_to_file.txt') that has its keys and values accessible as collection items and
as attributes. Example:
storage['name'] # will be string 'kek'
storage.song_name # will be 'shadilay'
storage.power # will be integer 9001

In case of attribute clash existing built-in attributes take precedence.
In case when value cannot be assigned to an attribute (for example when there's a line 1=something) ValueError should
be raised. File size is expected to be small, you are permitted to read it entirely into memory.
"""


class KeyValueStorage:
    def check_key(self, key):
        if key in self.__dir__():
            raise NameError(
                "Attribute name conflicts with existing one built-in attribute"
            )
        if not key.isidentifier():
            raise ValueError("This name cannot be assigned as an attribute name")

    def __init__(self, path: str):
        self._storage = {}

        with open(path, "r") as f:
            for line in f:
                key, value = line.rstrip().split("=")
                self.check_key(key)
                if value.isdigit():
                    value = int(value)
                self._storage[key] = value

    def __getattr__(self, item):
        if item in self._storage:
            return self._storage[item]
        return self.__getattribute__(item)

    def __getitem__(self, item):
        return self._storage[item]
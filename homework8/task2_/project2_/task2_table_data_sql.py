"""
Task.

Write a wrapper class TableData for database table, that when initialized with database name and table acts as
collection object (implements Collection protocol). Assume all data has unique values in 'name' column.
So, if presidents = TableData(database_name='example.sqlite', table_name='presidents')

then
--len(presidents) will give current amount of rows in presidents table in database
--presidents['Yeltsin'] should return single data row for president with name Yeltsin
--'Yeltsin' in presidents should return if president with same name exists in table
object implements iteration protocol. i.e. you could use it in for loops::
--for president in presidents:
----print(president['name'])
all above mentioned calls should reflect most recent data. If data in table changed after you created collection
instance, your calls should return updated data.
Avoid reading entire table into memory. When iterating through records, start reading the first record,
then go to the next one, until records are exhausted. When writing tests, it's not always neccessary to mock database
calls completely. Use supplied example.sqlite file as database fixture file.
"""

import sqlite3
from typing import Iterator


class TableData:
    def __init__(self, database_name: str, table_name: str) -> None:
        self.database_name = database_name
        self.table_name = table_name

    def __connect_to_database(self, query: str):
        with sqlite3.connect(self.database_name) as connection:
            cursor = connection.cursor()
            return cursor.execute(query.format(self.table_name))

    def __len__(self) -> int:
        return self.__connect_to_database(query="SELECT count(*) FROM {}").fetchone()[0]

    def __getitem__(self, item: str) -> tuple:
        data = self.__connect_to_database(query="SELECT * FROM {}")
        for line in data:
            if line[0] == item:
                return line
        raise KeyError("Item is not in database")

    def __contains__(self, item: str) -> bool:
        data = self.__connect_to_database(query="SELECT * FROM {}")
        for line in data:
            if line[0] == item:
                return True
        return False

    def __iter__(self) -> Iterator:
        return self.__connect_to_database(query="SELECT * FROM {}")

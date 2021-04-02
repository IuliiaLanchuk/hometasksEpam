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
from typing import Callable, Iterator


class TableData:
    def __init__(self, database_name: str, table_name: str) -> None:
        self.database_name = database_name
        self.table_name = table_name

    def execute_query(self, query: str, query_args: tuple, fetch: Callable):
        connection = sqlite3.connect(self.database_name)
        cursor = connection.cursor()
        cursor.execute(query.format(*query_args))
        result = fetch(cursor)
        connection.close()
        return result

    def __len__(self) -> int:
        return self.execute_query(
            "SELECT count(*) FROM '{}'",
            (self.table_name,),
            lambda cursor: cursor.fetchone()[0],
        )

    def __getitem__(self, item: str) -> tuple:
        return self.execute_query(
            "SELECT * FROM '{}' WHERE name = '{}'",
            (self.table_name, item),
            lambda cursor: cursor.fetchone(),
        )

    def __contains__(self, item: str) -> bool:
        return self.__getitem__(item) is not None

    def __iter__(self) -> Iterator:
        return self.execute_query(
            "SELECT * FROM '{}'",
            (self.table_name,),
            lambda cursor: iter(cursor.fetchall()),
        )
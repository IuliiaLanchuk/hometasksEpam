"""
Написать декоратор instances_counter, который применяется к любому классу
и добавляет ему 2 метода:
get_created_instances - возвращает количество созданых экземпляров класса
reset_instances_counter - сбросить счетчик экземпляров,
возвращает значение до сброса
Имя декоратора и методов не менять
Ниже пример использования
"""


def instances_counter(cls):
    """Is a decorator that implemented for each class that adds two methods to sent class."""

    class ClassHelper(cls):
        """Adds two additional methods to parent class to count created instances and reset this counter."""

        __instances_amount = 0

        def __init__(self, *args):
            super().__init__(*args)
            self.__class__.__instances_amount += 1

        @classmethod
        def get_created_instances(cls) -> int:
            """Return amount of instances created in sent class."""
            return cls.__instances_amount

        @classmethod
        def reset_instances_counter(cls) -> int:
            """Return amount of instances created in sent class before amount reset."""
            to_return = cls.get_created_instances()
            cls.__instances_amount = 0
            return to_return

    return ClassHelper

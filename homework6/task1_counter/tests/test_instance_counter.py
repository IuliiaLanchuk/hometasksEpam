from project1_counter.instance_counter import instances_counter


@instances_counter
class User:
    pass


@instances_counter
class Automobile:
    instances_amount = "black"

    def __init__(self, year):
        self.year = year

    def some_method(self):
        return self.year


def test_user_class_create_instances_and_reset_instance():
    assert User.get_created_instances() == 0
    user, _, _ = User(), User(), User()
    assert user.get_created_instances() == 3
    assert user.reset_instances_counter() == 3


def test_reset_instances_amount_to_zero():
    user, _ = User(), User()
    assert user.reset_instances_counter() == 2
    assert user.get_created_instances() == 0


def test_automobile_class_intricate_attributes_and_methods_do_not_change():
    opel_astra = Automobile(1998)
    assert opel_astra.instances_amount == "black"
    assert opel_astra.some_method() == 1998
    assert opel_astra.get_created_instances() == 1
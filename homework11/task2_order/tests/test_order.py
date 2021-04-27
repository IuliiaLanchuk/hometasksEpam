from project_hw11_task2.task_order import Order, elder_discount, morning_discount


def test_order_with_morning_discount():
    order_1 = Order(100, morning_discount)
    assert order_1.final_price() == 50.0


def test_order_with_elder_discount():
    order_2 = Order(100, elder_discount)
    assert order_2.final_price() == 10.0


def test_order_with_no_discount():
    order_3 = Order(180)
    assert order_3.final_price() == 180.0

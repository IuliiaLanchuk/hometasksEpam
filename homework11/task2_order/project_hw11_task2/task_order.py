"""
You are given the following code:
class Order:
    morning_discount = 0.25
    def __init__(self, price):
        self.price = price
    def final_price(self):
        return self.price - self.price * self.morning_discount
Make it possible to use different discount programs.
Hint: use strategy behavioural OOP pattern.
https://refactoring.guru/design-patterns/strategy
Example of the result call:
def morning_discount(order):
    ...
def elder_discount(order):
    ...
order_1 = Order(100, morning_discount)
assert order_1.final_price() == 50
order_2 = Order(100, elder_discount)
assert order_1.final_price() == 10
"""
from typing import Callable


class Order:
    def __init__(self, price: float, discount_strategy: Callable = None):
        self.price = price
        self.discount_strategy = discount_strategy if discount_strategy else no_discount

    def final_price(self) -> float:
        return self.discount_strategy(self)


def morning_discount(order):
    return order.price - order.price * 0.5


def elder_discount(order):
    return order.price - order.price * 0.9


def no_discount(order):
    return float(order.price)

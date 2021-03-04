# This sample tests the handling of if/elif chains that omit an else
# statement. The "ghost" else statement should be assumed never taken if the
# final if/elif test expression evaluates to Never in the negative case.

from enum import Enum
from typing import Literal, Union


def func1(x: Union[int, str]):
    if isinstance(x, int):
        y = 0
    elif isinstance(x, str):
        y = 1

    print(y)


def func2(x: Literal[1, 2, 3, 4]):
    if x == 1 or x == 2:
        y = 0
    elif x == 3 or not x == 3:
        y = 1

    print(y)


def func3(x: Literal[1, 2], y: Literal["one", "two"]):
    if x == 1 or y != "two":
        z = 0
    elif x == 2 or y != "one":
        z = 1

    print(z)


class Color(Enum):
    RED = 1
    BLUE = 2
    GREEN = 3
    PERIWINKEL = 4


def func4(x: Color):
    if x == Color.RED:
        return

    if x == Color.GREEN or (Color.PERIWINKEL == x and True):
        y = 2
    else:
        if Color.BLUE == x:
            y = 3

    print(y)


def func5():
    if True:
        y = 2

    print(y)


def func6():
    if not None:
        y = 2

    print(y)

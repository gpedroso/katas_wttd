"""
Regras di Fizzbuzz

1. Se a posição for múltiplo de 3, fale fizz.
2. Se a posição for múltiplo de 5, fale buzz.
3. Se a posição for múltiplo de 3 e 5, fale fizzbuzz.
4. Para qualquer outra posição fale o próprio número.

"""
from functools import partial

multiple_of = lambda base, num: num % base == 0
multiple_of_5 = partial(multiple_of, 5)
multiple_of_3 = partial(multiple_of, 3)

"""
def multiple_of_5(num):
    return multiple_of(5, num)

def multiple_of_3(num):
    return multiple_of(3, num)
"""

def robot(pos):
    say = str(pos)

    if multiple_of_5(pos) or multiple_of_3(pos):
        say = 'fizzbuzz'
    elif multiple_of_5(pos):
        say = 'buzz'
    elif multiple_of_3(pos):
        say = 'fizz'
    return say

def assert_equal(first, second, line):
    msg = "Fail: Line {} get {} expecting {}"
    try:
        assert first == second
    except AssertionError:
        print(msg.format(line, first,  second))

if __name__ == '__main__':
    assert_equal(robot(1), '1', 42)
    assert_equal(robot(2), '2', 43)
    assert_equal(robot(4), '4', 44)

    assert_equal(robot(3), 'fizz', 46)
    assert_equal(robot(6), 'fizz', 47)
    assert_equal(robot(9), 'fizz', 48)

    assert_equal(robot(5), 'buzz', 50)
    assert_equal(robot(10), 'buzz', 51)
    assert_equal(robot(20), 'buzz', 52)

    assert_equal(robot(15), 'fizzbuzz', 54)
    assert_equal(robot(30), 'fizzbuzz', 55)
    assert_equal(robot(45), 'fizzbuzz', 56)
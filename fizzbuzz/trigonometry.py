import math

from fizzbuzz.checks import check_function


def fizz_buzz(n: int) -> str:
    fizz = 'fizz' * int(math.cos(n * math.tau / 3))
    buzz = 'buzz' * int(math.cos(n * math.tau / 5))
    return (fizz + buzz) or str(n)


def test_trigonometry():
    check_function(fizz_buzz)


if __name__ == "__main__":
    test_trigonometry()
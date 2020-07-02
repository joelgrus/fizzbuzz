import itertools

from fizzbuzz.checks import check_output


fizzes = itertools.cycle(['', '', 'fizz'])
buzzes = itertools.cycle(['', '', '', '', 'buzz'])
numbers = itertools.count(1)

fizz_buzzes = ((fizz + buzz) or str(n)
                for fizz, buzz, n in zip(fizzes, buzzes, numbers))

output = [next(fizz_buzzes) for _ in range(100)]


def test_infinite_iterables():
    check_output(output)
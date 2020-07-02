from fizzbuzz.checks import check_function

CYCLE_OF_15 = ['fizzbuzz', None, None, 'fizz', 
               None, 'buzz', 'fizz', None, 
               None, 'fizz', 'buzz', None, 
               'fizz', None, None]


def fizz_buzz(n: int) -> str:
    return CYCLE_OF_15[n % 15] or str(n)


def test_cycle_of_15():
    check_function(fizz_buzz)
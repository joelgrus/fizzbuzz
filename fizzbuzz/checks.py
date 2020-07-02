from typing import Callable, List

FIZZ_BUZZ = [
    '1', '2', 'fizz', '4', 'buzz', 'fizz', '7', '8', 'fizz',
    'buzz', '11', 'fizz', '13', '14', 'fizzbuzz', '16', '17',
    'fizz', '19', 'buzz', 'fizz', '22', '23', 'fizz', 'buzz',
    '26', 'fizz', '28', '29', 'fizzbuzz', '31', '32', 'fizz',
    '34', 'buzz', 'fizz', '37', '38', 'fizz', 'buzz', '41',
    'fizz', '43', '44', 'fizzbuzz', '46', '47', 'fizz', '49',
    'buzz', 'fizz', '52', '53', 'fizz', 'buzz', '56', 'fizz',
    '58', '59', 'fizzbuzz', '61', '62', 'fizz', '64', 'buzz',
    'fizz', '67', '68', 'fizz', 'buzz', '71', 'fizz', '73',
    '74', 'fizzbuzz', '76', '77', 'fizz', '79', 'buzz',
    'fizz', '82', '83', 'fizz', 'buzz', '86', 'fizz', '88',
    '89', 'fizzbuzz', '91', '92', 'fizz', '94', 'buzz',
    'fizz', '97', '98', 'fizz', 'buzz'
]


def check_output(output: List[str]) -> None:
    assert len(output) == 100, "output should have length 100"

    # Collect all the errors in a list
    # The i+1 reflects that output[0] is the output for 1,
    # output[1] is the output for 2, and so on
    errors = [
        f"({i+1}) predicted: {output[i]}, actual: {FIZZ_BUZZ[i]}"
        for i in range(100)
        if output[i] != FIZZ_BUZZ[i]
    ]

    # And assert that the list of errors is empty
    assert not errors, f"{errors}"


def check_function(fizz_buzz: Callable[[int], str]) -> None:
    """
    The type annotation says that `fizz_buzz` needs to be 
    a function that takes a single argument (which is an `int`)
    and returns a `str`.
    """
    output = [fizz_buzz(i) for i in range(1, 101)]
    check_output(output)

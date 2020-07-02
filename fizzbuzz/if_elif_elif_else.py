from fizzbuzz.checks import check_function

def fizz_buzz(n: int) -> str:
    if n % 15 == 0:
        return 'fizzbuzz'
    elif n % 5 == 0:
        return 'buzz'
    elif n % 3 == 0:
        return 'fizz'
    else:
        return str(n)


def test_if_elif_elif_else():
    check_function(fizz_buzz)


if __name__ == "__main__":
    test_if_elif_elif_else()
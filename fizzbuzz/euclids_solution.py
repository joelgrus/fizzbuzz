from fizzbuzz.checks import check_function


def fizz_buzz(n: int) -> str:
    hi, lo = max(n, 15), min(n, 15)

    while hi % lo > 0:
        hi, lo = lo, hi % lo

    return {1: str(n), 3: "fizz", 5: "buzz", 15: "fizzbuzz"}[lo]


def test_euclids_solution():
    check_function(fizz_buzz)
    

if __name__ == "__main__":
    test_euclids_solution()
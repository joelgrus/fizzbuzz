import numpy as np

from fizzbuzz.checks import check_function


def fizz_buzz(n: int) -> str:
    w = np.array([[1, 0, 0], [2, -2, 0], [2, 0, -2], [3, -3, -3]])
    v = np.array([1, n % 3, n % 5])
    return [str(n), 'fizz', 'buzz', 'fizzbuzz'][np.argmax(w @ v)]


def test_matrix_multiplication():
    check_function(fizz_buzz)


if __name__ == "__main__":
    test_matrix_multiplication()
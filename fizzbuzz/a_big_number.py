import re

from fizzbuzz.checks import check_output


big_number = 0x134591c9a2c8e4d1647268b23934591c9a2c8e4d16

chunks = re.findall('(0|10|110|111)', f"{big_number:0>167b}")


def label(chunk: str, n: int) -> str:
    labels = [str(n), '', 'fizz', '', '', '', 'buzz', 'fizzbuzz']
    return labels[int(chunk, 2)]


output = [label(chunk, n+1) for n, chunk in enumerate(chunks)]


def test_big_number():
    check_output(output)


if __name__ == "__main__":
    test_big_number()
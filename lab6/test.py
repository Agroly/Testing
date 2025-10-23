import pytest
from Calculator import Calculator

@pytest.fixture
def calc():
    return Calculator()


@pytest.mark.parametrize(
    "a,b,expected",
    [
        (1, 2, 3),
        (-1, 5, 4),
        (0, 0, 0),
        (2.5, 3.5, 6.0),
        (-3, -7, -10)
    ]
)
def test_add(calc, a, b, expected):
    assert calc.add(a, b) == expected


@pytest.mark.parametrize(
    "a,b,expected,expect_exception",
    [
        (10, 2, 5, None),
        (7, 7, 1, None),
        (5, 2, 2.5, None),
        (5, 0, None, ValueError),
        (-10, -2, 5, None)
    ]
)
def test_divide(calc, a, b, expected, expect_exception):
    if expect_exception:
        with pytest.raises(expect_exception):
            calc.divide(a, b)
    else:
        assert calc.divide(a, b) == expected


@pytest.mark.parametrize(
    "n,expected",
    [
        (2, True),
        (3, True),
        (4, False),
        (17, True),
        (1, False),
        (0, False),
        (-5, False),
        (19, True),
        (20, False)
    ]
)
def test_is_prime_number(calc, n, expected):
    assert calc.is_prime_number(n) == expected

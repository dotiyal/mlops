from square_function_for_testing import get_square


def test_square():
    a = 4
    result = get_square(a)
    assert result == 16

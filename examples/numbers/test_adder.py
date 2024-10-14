import pytest
from adder import add
from expects import equal, expect


class TestAdder:
    @pytest.mark.parametrize(
        "x,y,expected",
        [
            (1, 2, 3),
            (2, 2, 4),
            (10, 100, 110),
        ],
    )
    def test_add(self, x, y, expected):
        result = add(x, y)

        expect(result).to(equal(expected))

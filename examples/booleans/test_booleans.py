import pytest
from expects import be_false, be_true, expect

from booleans import has_permission, is_even, is_truthy


class TestBooleans:
    @pytest.mark.parametrize(
        "value",
        [
            True,
            1,
            "Hello",
            [1, 2, 3],
            (1, "x"),
        ],
    )
    def test_is_truthy(self, value):
        expect(is_truthy(value)).to(be_true)

    @pytest.mark.parametrize(
        "value",
        [
            False,
            0,
            "",
            [],
            (),
            None,
        ],
    )
    def test_is_falsy(self, value):
        expect(is_truthy(value)).to(be_false)

    def test_has_permission(self):
        expect(has_permission(True, False)).to(be_false)
        expect(has_permission(True, True)).to(be_true)
        expect(has_permission(False, False)).to(be_false)

    def test_is_even(self):
        expect(is_even(4)).to(be_true)
        expect(is_even(5)).to(be_false)

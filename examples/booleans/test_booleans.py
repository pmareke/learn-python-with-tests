from expects import be_false, be_true, expect

from booleans import (
    MyObject,
    can_access_feature,
    has_permission,
    is_even,
    is_list_empty,
    is_truthy,
)


class TestBooleans:
    def test_is_even(self):
        expect(is_even(4)).to(be_true)
        expect(is_even(5)).to(be_false)

    def test_has_permission(self):
        expect(has_permission(True, False)).to(be_false)
        expect(has_permission(True, True)).to(be_true)
        expect(has_permission(False, False)).to(be_false)

    def test_can_access_feature(self):
        expect(can_access_feature(True, 21)).to(be_true)
        expect(can_access_feature(False, 10)).to(be_false)
        expect(can_access_feature(True, 17)).to(be_true)

    def test_is_truthy(self):
        expect(is_truthy(1)).to(be_true)
        expect(is_truthy(0)).to(be_false)
        expect(is_truthy("Hello")).to(be_true)
        expect(is_truthy("")).to(be_false)
        expect(is_truthy([])).to(be_false)
        expect(is_truthy([1, 2, 3])).to(be_true)
        expect(is_truthy(None)).to(be_false)

    def test_is_list_empty(self):
        expect(is_list_empty([])).to(be_true)
        expect(is_list_empty([1, 2, 3])).to(be_false)

    def test_custom_object_truthiness(self):
        obj1 = MyObject(0)

        expect(bool(obj1)).to(be_false)

        obj2 = MyObject(5)

        expect(bool(obj2)).to(be_true)

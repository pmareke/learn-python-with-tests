from expects import equal, expect

from lists import add


class TestList:
    def test_add(self):
        list = add([], 1)
        list = add(list, 2)

        expect(list).to(equal([1, 2]))

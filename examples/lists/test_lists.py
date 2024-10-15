from expects import equal, expect

from lists import add, remove


class TestList:
    def test_add(self):
        list = add([], 1)
        list = add(list, 2)

        expect(list).to(equal([1, 2]))

    def test_remove(self):
        list = [1, 2, 3]

        list = remove(list, 2)

        expect(list).to(equal([1, 3]))

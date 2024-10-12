from expects import equal, expect


class TestFoo:
    def test_bar(self) -> None:
        expect(1).to(equal(1))

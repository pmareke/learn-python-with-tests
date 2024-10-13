from expects import equal, expect

from hello import hello


class TestHello:
    def test_hello(self):
        expect(hello()).to(equal("Hello, world"))

from expects import equal, expect

from hello import Hello


class TestHello:
    def test_hello(self) -> None:
        hello = Hello()

        expect(hello.hello()).to(equal("Hello, world"))

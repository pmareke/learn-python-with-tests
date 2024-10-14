---
title: Numbers
weight: 3
---

**[You can find all the code for this chapter here](https://github.com/pmareke/learn-python-with-tests/tree/main/examples/numbers)**

Numbers in Python work as you would expect. There are two main types:

- `int` for integer numbers.
- `float` for decimal numbers.

> **Note:** There is also the [complex](https://docs.python.org/3/library/functions.html#complex) type, but we won't be covering that here.

### Operators

Python is actualy quite normal regarding numbers, you can apply them the typical operations like:

- `+` for addition.
- `-` for subtraction.
- `*` for multiplication.
- `/` for division.
- `//` for integer division.
- `%` for modulo.
- `**` for exponentiation.

So let's write an `add` function to try things out and play a little bit with them!.

Create a test file called `test_adder.py` and write this code.

### Write the test first

```python
from expects import equal, expect


class TestAdder:
    def test_add(self):
        result = add(1, 2)

        expect(result).to(equal(3))
```

### Try and run the test

```sh
================= short test summary info ================= 
FAILED test_adder.py::TestAdder::test_add
NameError: name 'add' is not defined
================= 1 failed in 0.02s ============
```

### Write the minimal amount of code to make it run

Write enough code to satisfy the compiler and that's all - remember we want to check that our tests fail for the correct reason.

```python
def add(a, b):
    pass
```

If we run the test again we should see a different error.

```sh
E       expected: None to be 2
================= short test summary info ================= 
FAILED test_adder.py::TestAdder::test_add
AssertionError: 
================= 1 failed in 0.02s ============
```

### Write enough code to make it pass

In the strictest sense of TDD we should now write the minimal amount of code to make the test pass. A pedantic programmer may do this

```python
def add(a, b):
    return 3
```

If we run the test again it should pass.

```sh
========================= 1 passed in 0.01s ========================= 
```

### Refactor

We could write another test, with some different numbers to force that test to fail but that feels.

Or we can parametrize the test to make it more flexible.

```python
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
```

If you now run the tests you should see them fail.

```sh
================= short test summary info ================= 
...
E       expected: 4 to be 3
FAILED test_adder.py::TestAdder::test_add
AssertionError: 

...

E       expected: 110 to be 3
FAILED test_adder.py::TestAdder::test_add
AssertionError: 
...
================= 1 failed in 0.02s ============
```

Let's fix it!

```python
def add(a, b):
    return a + b
```

```sh
========================= 3 passed in 0.01s ========================= 
```

## Wrapping up

What we have covered:

- More practice of the TDD workflow.
- Integers, Decimals, addition.
- Principal numbers operations in Python.

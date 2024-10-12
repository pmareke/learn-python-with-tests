---
title: Install Pytest
weight: 4
---

# Install Pytest

For this book we're going to use [Pytest](https://docs.pytest.org/en/6.2.x/contents.html) 
as the testing framerwork and [expects](https://expects.readthedocs.io) as our assertion library. 

## How to install Pytest and Expects

In order to add a new library in our project we just need to run the following command:

```sh
poetry add pytest expects
```

If everything works fine now we're in a position to create our first test.

## Validate Pytest is installed

**[You can find all the code for this chapter here](https://github.com/pmareke/learn-python-with-tests/tree/main/examples/test_foo.py)**

Once you have Pytest installed you need to create
a new file called `test_foo.py` inside the `src` folder with the following code
(*right now don't care about it!*):

```python
from expects import expect, equal

class TestFoo:
  def test_bar(self) -> None:
        expect(1).to(equal(1))
```
Save the file and run the following command in the terminal:

```sh
poetry run pytest
```

You should see something like these results:

```sh
test_foo.py .                                        [100%]
==================== 1 passed in 0.01s ====================
```

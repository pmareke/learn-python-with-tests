---
title: Hello World
weight: 1
---

**[You can find all the code for this chapter here](https://github.com/pmareke/learn-python-with-tests/tree/main/examples/hello)**

It is traditional for your first program in a new language to be [Hello, World](https://en.m.wikipedia.org/wiki/%22Hello,_World!%22_program).

- Create a folder wherever you like.
- Create a new file in it called `hello.py` and put the following code inside it:

```python
def hello():
    print("Hello, world")


hello()
```

To run it type `python hello.py`.

## How it works

When you write a program in Python you just can define a method and after that just call it.

The `def` keyword is how you define a function with a name and a body.

Python provide out of the box a function called `print` that we use to print out to the console.

## How to test

How do you test this? It is good to separate your "domain" code from the outside world \(side-effects\).

The `print` is a side effect \(printing to stdout\) and the string we send in is our domain.

So let's separate these concerns so it's easier to test

```python
def hello():
    return "Hello, world"


print(hello())
```

We have created a new function again with `def` called hello.

Now create a new file called `test_hello.py` where we are going to write a test for our `hello` function

```python
from expects import equal, expect

from hello import hello


class TestHello:
    def test_hello(self):
        expect(hello()).to(equal("Hello, world"))
```

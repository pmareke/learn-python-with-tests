---
title: Booleans
weight: 2
---

**[You can find all the code for this chapter here](https://github.com/pmareke/learn-python-with-tests/tree/main/examples/booleans)**

> **Note:** In order to make our tests more dynamic, we're going to `parametrize` them using `pytest`, more info [here](https://docs.pytest.org/en/stable/how-to/parametrize.html).

## Truthy and Falsy in Python

In Python, there are a few values that are considered falsy, and everything else is truthy.

Let's validate this hypothesis with some tests:

```python
@pytest.mark.parametrize(
    "value",
    [
        True,
        1,
        "Hello",
        [1, 2, 3],
        (1, "x")
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
```

Let's implement the `is_truthy` function:

```python
def is_truthy(value):
    return bool(value)
```

We can say now that:

- `True`, `1`, `strings with values`, and `lists and tuples with items` are **truthy**.
- `False`, `0`, `""`, `[]`, `()`, `None` are **falsy**.

## Write the test first

```python
def test_has_permission(self):
    expect(has_permission(True, False)).to(be_false)
```

## Try and run the test

## Write the minimal amount of code to make it run

```python
def has_permission(is_admin, is_logged_in):
    pass
```

## Write enough code to make it pass

```python
def has_permission(is_admin, is_logged_in):
    return false
```
## Refactor

```python
def test_has_permission(self):
    expect(has_permission(True, False)).to(be_false)
    expect(has_permission(True, True)).to(be_true)
    expect(has_permission(False, False)).to(be_false)
```

```python
def has_permission(is_admin, is_logged_in):
    return is_admin and is_logged_in
```

## Write the test first

```python
def test_is_even(self):
    expect(is_even(4)).to(be_true)
```

## Try and run the test

## Write the minimal amount of code to make it run

```python
def is_even(n):
    pass
```

## Write enough code to make it pass

```python
def is_even(n):
    return True
```
## Refactor

```python
def test_is_even(self):
    expect(is_even(4)).to(be_true)
    expect(is_even(5)).to(be_false)
```

```python
def is_even(n):
    return n % 2 == 0
```

## Wrapping up

What we have covered:

- Parametrize our tests in order to test multiple cases.
- More practice of the TDD workflow.
- What is truthy and falsy in Python.
- The `and` and `or` operators.

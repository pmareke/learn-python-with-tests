---
title: Booleans
weight: 2
---

**[You can find all the code for this chapter here](https://github.com/pmareke/learn-python-with-tests/tree/main/examples/booleans)**


## Truthy and Falsy in Python

In Python, there are a few values that are considered `falsy`, and everything else is `truthy`.

Let's validate our hypothesis with some tests:

> **Note:** In order to make our tests more dynamic, we're going to `parametrize` them using `pytest`, more info [here](https://docs.pytest.org/en/stable/how-to/parametrize.html).

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

Let's implement the `is_truthy` function just casting the value to a boolean:

```python
def is_truthy(value):
    return bool(value)
```

We can say now that as we assumed:

- `True`, `1`, strings with values, lists and tuples with item are **truthy**.
- `False`, `0`, `""`, `[]`, `()`, `None` are **falsy**.

## Boolean operators

In Python instead of `||` or `&&` operators, we have the `and` and `or` operators to combine boolean expressions.

### Write the test first

Let's say we have a function that checks if a user has permission to do something. 

The user must be an admin and logged in:

```python
def test_has_permission(self):
    expect(has_permission(is_admin=True, is_logged_in=False)).to(be_false)
```

### Try and run the test

```sh
================= short test summary info ================= 
FAILED test_booleans.py::TestBooleans::test_has_permission
NameError: name 'has_permission' is not defined
================= 1 failed in 0.02s ============
```

Pretty explanatory, we need to define the `has_permission` function.

### Write the minimal amount of code to make it run

The simplest implementation would be just create it without any logic:

```python
def has_permission(is_admin, is_logged_in):
    pass
```
Re-run the tests:

```sh
E       expected: None to be false
================= short test summary info ================= 
FAILED test_booleans.py::TestBooleans::test_has_permission
AssertionError: 
================= 1 failed in 0.02s ============
```

Now the problem is that we're not returning nothing, that's good.

Step by step, let's make the test pass.

### Write enough code to make it pass

Right now, we only have one test, so we can just return `False`:

```python
def has_permission(is_admin, is_logged_in):
    return False
```

And the test passes:

```sh
========================= 1 passed in 0.01s ========================= 
```

### Refactor

Now we can add more cases to our test in order to make our function working as expected:

```python
def test_has_permission(self):
    expect(has_permission(True, False)).to(be_false)
    expect(has_permission(True, True)).to(be_true)
    expect(has_permission(False, False)).to(be_false)
```

Re-run the tests in order to see them failing.

After that we can implement the `has_permissions` function:

```python
def has_permission(is_admin, is_logged_in):
    return is_admin and is_logged_in
```

## Comparing values

Regardig the comparison of values, we can use the `==` operator to compare two values as in many other languages, nothing relevante here actually.

So just let's write a test to check if a number is even or not.

> **Note:** We need to make muscle, so let's repeat the process again (`Red - Green - Refactor`)

### Write the test first

```python
def test_is_even(self):
    expect(is_even(4)).to(be_true)
```

### Try and run the test

```sh
================= short test summary info ================= 
FAILED test_booleans.py::TestBooleans::test_is_even
NameError: name 'is_even' is not defined
================= 1 failed in 0.02s =======================
```

### Write the minimal amount of code to make it run

```python
def is_even(n):
    pass
```

```sh
E       expected: None to be true
================= short test summary info ================= 
FAILED test_booleans.py::TestBooleans::test_is_even
AssertionError: 
================= 1 failed in 0.02s =======================
```

### Write enough code to make it pass

```python
def is_even(n):
    return True
```

```sh
=================== 1 passed in 0.01s ==================== 
```

### Refactor

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
- Comparing values.

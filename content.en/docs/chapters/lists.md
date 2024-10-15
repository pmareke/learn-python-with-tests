---
title: Lists
weight: 4
---

**[You can find all the code for this chapter here](https://github.com/pmareke/learn-python-with-tests/tree/main/examples/lists)**

Lists in Python are a collection of items that can be of different types. They are mutable, meaning that you can change the elements 
in a list after you have created it.

It's possible to operate them in different ways, like adding, removing, or checking if an element is in the list.

The access is made by an index, which is an integer that represents the position of the element in the list. The index starts at 0.

Enough talk, let's implement the `add` operation.

### Write the test first

As always, we start by writing a test that describes the behavior we want to implement.

```python
from expects import expect, equal


class TestList:
    def test_add(self):
        list = add([], 1)

        expect(list).to(equal([1]))
```

### Try and run the test

If we run the test, we should see an error.

```sh
================= short test summary info ================= 
FAILED test_list.py::TestList::test_list
NameError: name 'add' is not defined
================= 1 failed in 0.02s =======================
```

### Write the minimal amount of code to make it run

Let's implement the `add` function with the enough code to make the test compile.

```python
def add(list, item):
    pass
```
If we run the test again we should see a different error.

```sh
E       expected: None to be [1]
================= short test summary info ================= 
FAILED test_list.py::TestList::test_list
AssertionError: 
================= 1 failed in 0.02s ============
```

### Write enough code to make it pass

Now it's time to write the code that makes the test pass.

```python
def add(list, item):
    return [item]
```

If we run the test again it should pass.

```sh
========================= 1 passed in 0.01s ========================= 
```

### Refactor

Let's add more items in the list, which will force us to refactor the code.

```python
from expects import expect, equal


class TestList:
    def test_add(self):
        list = add([], 1)
        list = add(list, 2)

        expect(list).to(equal([1, 2]))
```

Finally, we can refactor the code to make it more general.

```python
def add(list, item):
    return list + [item]
```

## Wrapping up

What we have covered:

- More practice of the TDD workflow.
- Working with lists.

## Your turn

A great way to learn is doing, so here are some ideas to keep practicing:

- Write a test for the other operations like **remove** an item on the list, calculate the **length** of a list or **check**
if a list contains an item.

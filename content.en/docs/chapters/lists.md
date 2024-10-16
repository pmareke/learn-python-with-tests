---
title: Lists
weight: 4
---

**[You can find all the code for this chapter here](https://github.com/pmareke/learn-python-with-tests/tree/main/examples/lists)**

Lists in Python are a collection of items that can be of different types. They are mutable, meaning that you can change the elements 
in a list after you have created it.

It's possible to operate them in different ways, like adding, removing, or checking if an element is in the list.

The access is made by an index, which is an integer that represents the position of the element in the list. The index starts at 0.

## Add an item to a list

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

## Remove an item from a list

What about removing an item from a list? Let's give it a try!

### Write the test first

As always, we start by writing a test that describes the behavior we want to implement.

```python
from expects import expect, equal


class TestList:
    def test_remove(self):
        list = [1, 2, 3]
        list = remove(list, 1)

        expect(list).to(equal([2, 3]))
```

### Try and run the test

If we run the test, we should see an error.

```sh
================= short test summary info ================= 
FAILED test_list.py::TestList::test_remove
NameError: name 'remove' is not defined
================= 1 failed in 0.02s =======================
```

### Write the minimal amount of code to make it run

Let's implement the `remove` function with the enough code to make the test compile.

```python
def remove(list, item):
    pass
```
If we run the test again we should see a different error.

```sh
E       expected: None to be [2, 3]
================= short test summary info ================= 
FAILED test_list.py::TestList::test_remove
AssertionError: 
================= 1 failed in 0.02s ============
```

### Write enough code to make it pass

Now it's time to write the code that makes the test pass.

```python
def remove(list, item):
    return [2 ,3]
```

If we run the test again it should pass.

```sh
========================= 1 passed in 0.01s ========================= 
```

### Refactor

Let's remove more items in the list, which will force us to refactor the code.

```python
from expects import expect, equal
from list import remove


class TestList:
    def test_add(self):
        list = [1, 2 ,3]

        list = remove(list, 2)
        list = remove(list, 3)

        expect(list).to(equal([1]))
```

Finally, we can refactor the code to make it more general.

```python
def remove(list, item):
    new_list = []
    for i in list:
        if i != item:
            new_list = add(new_list, i)
    return new_list
```

> **Note**: We're using a `for` loop, don't worry about it we'll talk about it later in this book.

## Wrapping up

What we have covered:

- More practice of the TDD workflow.
- Working with lists, adding and removing items.

## Your turn

A great way to learn is doing, so here are some ideas to keep practicing:

- Write a test to calculate the **length** of a list.
- Write a test to **check** if a list contains an item.
- Write a test to **compare** two lists.

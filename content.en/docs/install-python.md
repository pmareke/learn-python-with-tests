---
title: Install Python
weight: 2
---

## How to install Python

There a couple of ways to install Python in your computer:

* You can go to the official [page](https://www.python.org/downloads/)
and follow the given instructions for your operation system.
* You can use the [asdf](https://asdf-vm.com).

## Validate Python is installed

Once you have Python installed you should be able to run the following command
in the terminal:

```sh
python --version # => Python 3.12.0
```

## Install Poetry

In this book we will be using [Poetry](https://python-poetry.org/) as our dependency manager.

In order to install Poetry you can run the following command:

```sh
curl -sSL https://install.python-poetry.org | python3 -
```

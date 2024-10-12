---
title: Prepare the project
weight: 3
---

# Prepare the project for this book

Once we have Python installed we need to create the folders
structure in which weŕe going to write the code for each
chapter.


## Create the folder for the chapters and its tests

To do so, we need to create a couple of folders with the 
following command:

```sh
mkdir tests src
```
## Create a new Python project

After that we're in position of creating the project using [poetry](https://python-poetry.org).

To do it, just run the following command in the terminal:

```sh
poetry init
```

This command will create a new file called `pyproject.toml` in which the dependencies will be saved.

```sh
poetry add pytest expects
```

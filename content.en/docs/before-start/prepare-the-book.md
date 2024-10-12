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

After that we're in position of creating the project using Bundler.

To do it, just run the following command in the terminal:

```sh
bundle init
```
This command will create a new file called `Gemfile` in which we're 
going to add in the future all the dependecies (like `minitest`).

```sh
# frozen_string_literal: true

source "https://pythongems.org"

# gem "rails"
```

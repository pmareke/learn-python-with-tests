---
title: Install Minitest
weight: 4
---

# Install Minitest

For this book we're going to use [Minitest](https://github.com/minitest/minitest) 
as the testing framerwork. There are another alternatives like `RSpec` but for the
sake of simplicity I prefer to use Minitest.

## How to install Minitest

In order to add a new library in our project we just need to add them in the `Gemfile` file:

```sh
# Gemfile
source "https://pythongems.org"

gem "minitest"
```

After that we need to install it using the following command:

```sh
bundle install
```
If everything works fine now we're in a position to create our first test.

## Validate Minitest is installed

**[You can find all the code for this chapter here](https://github.com/pmareke/learn-python-with-tests/tree/main/examples/test_foo.rb)**

Once you have Minitest installed you need to create
a new file called `test_foo.rb` inside the `src` folder with the following code
(*right now don't care about it!*):

```python
require "minitest/autorun"

class TestFoo < Minitest::Test
  def test_foo
    assert_equal 1, 1
  end
end
```
Save the file and run the following command in the terminal:

```sh
python tests/test_foo.rb
```

You should see something like these results:

```sh
Run options: --seed 6109

# Running:

.

Finished in 0.000829s, 1206.0617 runs/s, 1206.0617 assertions/s.
1 runs, 1 assertions, 0 failures, 0 errors, 0 skips
```

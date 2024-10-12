require 'minitest/autorun'

require_relative 'hello'

class TestHello < Minitest::Test
  def test_hello
    assert_equal hello, 'Hello, world'
  end
end

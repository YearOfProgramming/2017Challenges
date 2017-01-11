defmodule ReverseTest do
  use ExUnit.Case
  doctest Reverse

  test "input is reversed" do
    assert Reverse.reverse_string("joe") == "eoj"
  end
end

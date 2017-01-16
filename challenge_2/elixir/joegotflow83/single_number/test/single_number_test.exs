defmodule SingleNumberTest do
  use ExUnit.Case
  doctest SingleNumber

  test "first value is non repeating" do
    assert 1 == SingleNumber.unique([1, 2, 2, 3, 5, 5, 3, 6, 6])
  end

  test "middle value is non repeating" do
    assert 4 == SingleNumber.unique([9, 8, 9, 4, 5, 7, 5, 7, 8])
  end

  test "last value is non repeating" do
    assert 9 == SingleNumber.unique([10, 5, 3, 5, 3, 10, 9])
  end

  test "characters work as well" do
    assert "a" == SingleNumber.unique(["b", "b", 7, 9, "a", 9, 7])
  end

  test "if no unique elements exist" do
    assert "There are no unique elements." == SingleNumber.unique([1, 2, 3, 3, 2, 1])
  end
end

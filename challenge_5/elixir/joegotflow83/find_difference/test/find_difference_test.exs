defmodule FindDifferenceTest do
  use ExUnit.Case
  doctest FindDifference

  test "difference is spotted at end of line" do
    assert "e" == FindDifference.difference("abcd", "abcde")
  end

  test "difference is spotted at front of line" do
    assert "f" == FindDifference.difference("food", "ood")
  end

  test "difference is spotted at middle of line" do
    assert "z" == FindDifference.difference("thzpot", "thpot")
  end

  test "numbers in strings work as well" do
    assert "3" == FindDifference.difference("12345", "1245")
  end
end

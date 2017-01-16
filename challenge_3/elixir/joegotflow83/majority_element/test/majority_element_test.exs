defmodule MajorityElementTest do
  use ExUnit.Case
  doctest MajorityElement

  test "test major element is present" do
    assert 7 == MajorityElement.find_major_ele([2,2,3,7,5,7,7,7,4,7,2,7,4,5,6,7,7,8,6,7,7,8,10,12,29,30,19,10,7,7,7,7,7,7,7,7,7])
  end

  test "test no major element is present" do
    assert "No element is the majority." == MajorityElement.find_major_ele([2,2,2,1,2,2,4,5,6,7,8,9,7,5,3])
  end
end

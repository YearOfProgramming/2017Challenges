defmodule MajorityElement do
  def find_major_ele(input) when is_list(input) do
    input
    |> Enum.reduce(%{}, &count/2)
    |> Map.to_list
    |> determine_majority(length(input))
  end

  def determine_majority([head | tail], n) do
    {num, value} = head
    cond do
      value > (n / 2) ->
        num
      true ->
        determine_majority(tail, n)
    end
  end

  def determine_majority([], _n) do
    "No element is the majority."
  end

  def count(num, acc) do
    Map.update acc, num, 1, &(&1 + 1)
  end
end

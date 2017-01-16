defmodule SingleNumber do
  def unique(input) do
    input
    |> Enum.reduce(%{}, &count/2)
    |> Map.to_list
    |> find_uni
  end

  def find_uni([head | tail]) do
    case head do
      {num, 1} ->
        num
      _ ->
        find_uni(tail)
    end
  end

  def find_uni([]) do
    "There are no unique elements."
  end

  def count(num, acc) do
    Map.update acc, num, 1, &(&1 + 1)
  end
end

defmodule Reverse do
  @moduledoc """
  Year of Programming 2017 challenge 1.
  """

  @doc """  
  Reverse a string.

  ## Examples

      iex> Reverse.string "Hello"
      "olleH"
      
  """
  @spec string(String.t) :: String.t
  def string(value), do: do_string(String.next_graphem(value), [])

  defp do_string({head, tail}, acc), do: do_string(String.next_grapheme(tail), [head | acc])
  defp do_string(nil, acc), do: IO.iodata_to_binary(acc)
end
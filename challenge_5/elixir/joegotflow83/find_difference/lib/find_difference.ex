defmodule FindDifference do
  def difference(string1, string2) do
    string1 = string_to_list(string1)
    string2 = string_to_list(string2)
    cond do
      length(string1) < length(string2) ->
        check_char(string2, string1)
      length(string1) > length(string2) ->
        check_char(string1, string2)
    end
  end

  def check_char([head | tail], comp_string) do
    case Enum.member?(comp_string, head) do
      true ->
        check_char(tail, comp_string)
      false ->
        head
    end
  end

  def check_char([], _comp_string) do
    "The strings are identical"
  end

  def string_to_list(string) do
    String.graphemes(string)
  end
end

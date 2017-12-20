defmodule Hello do
  @moduledoc """
  Year of Programming 2017 challenge 0.
  """

  @doc """  
  Say hello to someone.

  ## Parameters

    - name: String that represents a name.  Defaults to "world".

  ## Examples

      iex> Hello.world
      "Hello, world!"

      iex> Hello.world "Rob"
      "Hello, Rob!"
      
  """
  @spec world(String.t) :: String.t
  def world(name \\ "world"), do: "Hello, #{name}!"
end

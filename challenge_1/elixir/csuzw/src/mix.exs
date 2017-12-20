defmodule Reverse.Mixfile do
  use Mix.Project

  def project do
    [app: :reverse,
     version: "0.1.0",
     elixir: "~> 1.4",
     build_embedded: Mix.env == :prod,
     start_permanent: Mix.env == :prod,
     deps: deps()]
  end

  def application do
    []
  end

  defp deps do
    [{:ex_doc, "~> 0.14.5", only: :dev}]
  end
end

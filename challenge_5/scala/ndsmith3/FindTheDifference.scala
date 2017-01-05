object FindTheDifference {
  def differentChar(original: String, mod: String): Char =
    mod.filterNot(x => original.contains(x)).head
}

object FindTheDifferenceApp extends App {
  println(FindTheDifference.differentChar("abcd", "abcde"))
}

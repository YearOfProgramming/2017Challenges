object StringReverse {
  def reverse(in: String, out: String = ""): String =
    if (in.isEmpty) out else reverse(in.tail, in.head + out)
}

object Challenge2 extends App {
  import StringReverse.reverse
  println(reverse(args.head))
}

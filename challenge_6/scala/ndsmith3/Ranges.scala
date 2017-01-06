import scala.annotation.tailrec

object Ranges {
  @tailrec
  def makeRangeString(answer: List[String])(curr: Array[Int]): List[String] = {
    val answerPlusNext       = (curr.head.toString :: answer)
    lazy val nextIsIncrement = curr.head + 1 != curr(1)
    lazy val lastIsDecrement = answer.head.toInt + 1 == curr.head
    curr.length match {
      case 1 if lastIsDecrement => answerPlusNext.reverse
      case 1                    => answer.reverse
      case _ if nextIsIncrement => answerPlusNext.reverse
      case _                    => makeRangeString(answerPlusNext)(curr.tail)
    }
  }

  def prettyRangeAndLast(range: List[String]): (String, Int) =
    (s"${range.head}->${range.last}", range.last.toInt)

  val makeStringifiedRange = prettyRangeAndLast _ compose makeRangeString(Nil) _

  @tailrec
  def ranges(ints: Array[Int], strings: List[String] = Nil): List[String] = {
    val (range, cutoff) = makeStringifiedRange(ints)
    val newInts         = ints.slice(ints.indexOf(cutoff) + 1, ints.length)
    if (newInts.length <= 1) (range :: strings).reverse
    else ranges(newInts, range :: strings)
  }
}

object Challenge6 extends App {
  def test(x: Array[Int]): Unit = println(Ranges.ranges(x))
  test(Array(1, 2, 3, 4, 8, 9, 10, 12, 13, 14))
  test(Array(1,2,3,4,9,10,15))
}

object Squares {
  // Lazy values are used in the sortSquares function to avoid exceptions from
  // arising in the case of soln or negSquares being empty. It also saves
  // computation time in this case.
  def square(ints: Array[Int]): Array[Int] = {
    val squares = ints.map(x => x * x)
    def sortSquares(currIndex: Int = 0,
                    soln: Array[Int] = Array(),
                    negSquares: List[Int] = Nil): Array[Int] = {
      lazy val negShouldBeTaken =
        !negSquares.isEmpty && negSquares.head <= squares(currIndex)
      lazy val popNegIntoSoln =
        sortSquares(currIndex, soln :+ negSquares.head, negSquares.tail)
      lazy val popPosIntoSoln =
        sortSquares(currIndex + 1, soln :+ squares(currIndex), negSquares)
      lazy val pushNegIntoStack =
        sortSquares(currIndex + 1, soln, squares(currIndex) :: negSquares)

      (currIndex - squares.length) match {
        case 0 if negSquares.isEmpty  => soln
        case 0                        => popNegIntoSoln
        case _ if ints(currIndex) < 0 => pushNegIntoStack
        case _ if negShouldBeTaken    => popNegIntoSoln
        case _                        => popPosIntoSoln
      }
    }
    sortSquares()
  }
}

object Challenge9 extends App {
  def test(arr: Array[Int]): Unit = println(Squares.square(arr).toList)

  test(Array(-2, -1, 0, 1, 2))
  test(Array(0, 1, 2))
  test(Array(-5, -4, -3, -2))
  test(Array(1, 2))
}

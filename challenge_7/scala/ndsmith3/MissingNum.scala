import scala.annotation.tailrec

object MissingNum {
  def missingNum(nums: Array[Int]): Int = {
    @tailrec
    def test(x: Int): Int = if (!nums.contains(x)) x else test(x + 1)
    test(0)
  }
}

object Challenge7 extends App {
  def test(arr: Array[Int]): Unit = println(MissingNum.missingNum(arr))
  test(Array(0, 1, 2, 4))
  test(Array(1, 2, 3))
}

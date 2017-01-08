import scala.annotation.tailrec

object MissingNum {
  def missingNum(nums: Array[Int]): Int = {
    def accu(currInt: Int, sum: Int = 0): Int =
      if (currInt == 0) sum else accu(currInt - 1, sum + currInt)

    val shouldBe = accu(nums.length)
    val is       = nums.sum
    shouldBe - is
  }
}

object Challenge7 extends App {
  def test(arr: Array[Int]): Unit = println(MissingNum.missingNum(arr))
  test(Array(0, 1, 2, 4))
  test(Array(1, 2, 3))
}

import scala.annotation.tailrec

object MissingNum {
  def missingNum(nums: Array[Int]): Int = {
    // Not sure if using (1 to nums.length).sum breaks the space requirement
    // of the challenge, so I'm using this accumluation function insteam
    def accu(currNums: Array[Int], sum: Int = 0): Int =
      if (currNums.isEmpty) sum else accu(currNums.tail, sum + currNums.head)

    val shouldBe = accu(nums)
    val is       = nums.sum
    shouldBe - is
  }
}

object Challenge7 extends App {
  def test(arr: Array[Int]): Unit = println(MissingNum.missingNum(arr))
  test(Array(0, 1, 2, 4))
  test(Array(1, 2, 3))
}

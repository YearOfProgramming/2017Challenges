object Majority {
  def majorityElement[A](elems: Array[A]): A = {
    def occurances(elem: A): Int = elems.filter(_ == elem).length
    val majorityThresh = elems.length / 2
    (elems filter (x => occurances(x) >= majorityThresh)).head
  }
}

object Challenge3 extends App {
  import Majority.majorityElement

  println(majorityElement(Array(2, 2, 3, 7, 5, 7, 7, 7, 4, 7, 2, 7, 4, 5, 6,
    7, 7, 8, 6, 7, 7, 8, 10, 12, 29, 30, 19, 10, 7, 7, 7, 7, 7, 7, 7, 7, 7)))
}

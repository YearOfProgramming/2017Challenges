object SingleNumber {
  def unique(elems: Array[Any], soln: List[Any] = Nil): List[Any] = {
    elems.length match {
      case 0 => soln
      case _ if elems.tail.contains(elems.head) =>
        unique(elems.filter(_ != elems.head), soln)
      case _ => unique(elems.tail, elems.head :: soln)
    }
  }
}

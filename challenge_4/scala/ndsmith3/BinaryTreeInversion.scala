trait Tree[+A] {
  val isEmpty: Boolean
  val isFull: Boolean

  lazy val inverted: Tree[A] = {
    this match {
      case EmptyTree()             => this
      case Node(elem, left, right) => Node(elem, right.inverted, left.inverted)
    }
  }

  def add[B >: A](elem: B): Tree[B] = {
    this match {
      case EmptyTree()                       => Node(elem)
      case Node(x, EmptyTree(), EmptyTree()) => Node(x, Node(elem))
      case Node(x, l, EmptyTree())           => Node(x, l, Node(elem))

      case Node(x, l, r) if l.isFull && r.isFull => Node(x, l.add(elem), r)
      case Node(x, l, r) if l.isFull             => Node(x, l, r.add(elem))
      case Node(x, l, r)                         => Node(x, l.add(elem), r)
    }
  }
}

case class EmptyTree[A]() extends Tree[A] {
  override val isEmpty = true
  override val isFull = false
}

case class Node[A](elem: A,
                   left: Tree[A] = EmptyTree(),
                   right: Tree[A] = EmptyTree())
    extends Tree[A] {
  override val isEmpty = false
  override val isFull      = !left.isEmpty && !right.isEmpty
}

object Challenge4 extends App {
  val tree = Node(4).add(2).add(7).add(1).add(3).add(6).add(9)
  println(tree)
  println(tree.inverted)
}

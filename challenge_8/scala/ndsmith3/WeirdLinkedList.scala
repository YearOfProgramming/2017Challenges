import scala.util.Random.nextInt

case class WeirdList[A](data: A) {
  var next: Option[WeirdList[A]] = None
  var rand: WeirdList[A]         = this
  var length: Int                = 1

  def add(data: A): Unit = {
    def assignRand(list: WeirdList[A])(
        index: Int = nextInt(this.length)): Unit = {
      if (index == this.indexOf(list.data)) assignRand(list)()
      else list.rand = this.subList(index)
    }

    this.next match {
      case None           => this.next = Option(WeirdList(data))
      case Some(nextNode) => nextNode.add(data)
    }
    if (this.length > 1) this foreach (x => assignRand(x)())
    length += 1
  }

  def addNode(node: WeirdList[A]): Unit = {
    this.next match {
      case None           => this.next = Option(node)
      case Some(nextNode) => nextNode.addNode(node)
    }
  }

  def indexOf(data: A, index: Int = 0): Int = {
    if (this.data == data) index
    else this.next match {
      case None           => throw new Exception("Element not found")
      case Some(nextNode) => nextNode.indexOf(data, index + 1)
    }
  }

  def subList(index: Int): WeirdList[A] =
    (1 to index).foldLeft(this)((x, _) => x.next.get)

  def foreach(f: WeirdList[A] => Unit): Unit = {
    f(this)
    this.next match {
      case None           => ()
      case Some(nextNode) => nextNode.foreach(f)
    }
  }

  override def toString(): String = {
    val end = this.next match {
      case None           => ""
      case Some(nextNode) => " :: " + nextNode.toString
    }
    data.toString + end
  }
}

object WeirdList {
  def copyProof[A](list: WeirdList[A]): WeirdList[String] = {
    def getData(curr: WeirdList[A] = list): List[(A, Option[Int], Int, Int)] = {
      val tuple = {
        val data = curr.data
        val nextIndex = curr.next match {
          case None            => None
          case Some(nextIndex) => Some(list.indexOf(nextIndex.data))
        }
        val randIndex = list.indexOf(curr.rand.data)
        val length    = curr.length
        (data, nextIndex, randIndex, length)
      }

      curr.next match {
        case None           => tuple :: Nil
        case Some(nextNode) => tuple :: getData(nextNode)
      }
    }

    val data  = getData()
    val nodes = data.map(x => WeirdList(x._1.toString + "'"))
    nodes foreach { x =>
      val dataObj = data(nodes.indexOf(x))
      x.next = dataObj._2.flatMap(x => Option(nodes(x)))
      x.rand = nodes(dataObj._3)
      x.length = dataObj._4
    }
    nodes.head
  }
}

object Challenge8 extends App {
  def listTest[A](test: WeirdList[A]): Unit = {
    println(test)
    test foreach (x => println(s"${x.data} -> ${x.rand}"))
  }

  val list = WeirdList(1)
  (2 to 5) foreach (x => list.add(x))
  val copyProof = WeirdList.copyProof(list)

  listTest(list)
  println()
  listTest(copyProof)
}

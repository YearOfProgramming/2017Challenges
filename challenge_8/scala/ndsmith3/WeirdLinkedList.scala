import scala.util.Random.nextInt

case class WeirdList[A](data: A) {
  var next: Option[WeirdList[A]] = None
  var rand: Option[WeirdList[A]] = None
  var length: Int                = 1

  def add(data: A): Unit = {
    def assignRand(list: WeirdList[A])(
        index: Int = nextInt(this.length)): Unit = {
      if (index == this.indexOf(list.data)) assignRand(list)()
      else list.rand = Option(this.subList(index))
    }

    if (this.next.isDefined) this.next.get.add(data)
    else this.next = Option(WeirdList(data))
    if (this.length > 1) this foreach (x => assignRand(x)())
    length += 1
  }

  def addNode(node: WeirdList[A]): Unit = {
    if (this.next.isDefined) this.next.get.addNode(node)
    else this.next = Option(node)
  }

  def indexOf(data: A, index: Int = 0): Int = {
    if (this.data == data) index
    else this.next.get.indexOf(data, index + 1)
  }

  def subList(index: Int): WeirdList[A] =
    (1 to index).foldLeft(this)((x, _) => x.next.get)

  def foreach(f: WeirdList[A] => Unit): Unit = {
    f(this)
    if (this.next.isDefined) this.next.get.foreach(f)
  }

  override def toString(): String = {
    val end = if (next.isDefined) " :: " + next.get.toString else ""
    data.toString + end
  }
}

object WeirdList {
  def copyProof[A](list: WeirdList[A]): WeirdList[String] = {
    def getData(curr: WeirdList[A] = list): List[(A, Option[Int], Int, Int)] = {
      val tuple = {
        val data = curr.data
        val nextIndex =
          if (curr.next.isDefined)
            Some(list.indexOf(curr.next.get.data))
          else None
        val randIndex = list.indexOf(curr.rand.get.data)
        val length    = curr.length
        (data, nextIndex, randIndex, length)
      }
      if (curr.next.isEmpty) tuple :: Nil
      else tuple :: getData(curr.next.get)
    }

    val data  = getData()
    val nodes = data.map(x => WeirdList(x._1.toString + "'"))
    nodes foreach { x =>
      val dataObj = data(nodes.indexOf(x))
      x.next = dataObj._2.flatMap(x => Option(nodes(x)))
      x.rand = Option(nodes(dataObj._3))
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

object ValidClosers {
  val closerMap = Map((')' -> '('), (']' -> '['), ('}' -> '{'))

  def hasValidClosers(str: String): Boolean = {
    def innerClosers(in: List[Char], stack: List[Char] = Nil): Boolean = {
      lazy val stackCloses      = !stack.isEmpty && stack.head == closerMap(in.head)
      lazy val continueWithPush = innerClosers(in.tail, in.head :: stack)
      lazy val continueWithPop  = innerClosers(in.tail, stack.tail)

      in match {
        case x :: _ if x == '(' || x == '[' || x == '{'    => continueWithPush
        case ')' :: _ | ']' :: _ | '}' :: _ if stackCloses => continueWithPop
        case Nil                                           => stack.isEmpty
        case _                                             => innerClosers(in.tail, stack)
      }
    }
    innerClosers(str.toCharArray.toList)
  }
}

object Challenge10 extends App {
  def test(str: String): Unit = println(ValidClosers.hasValidClosers(str))

  ("{{{{{{{{{adfkjaefia}}}}}}}" ::
    "{{{{{{{{{[[[[[[kadfa{{{{{{{((({daljfdaf({{{[]}}kaldjfs})})))}}}}}}}]]]]]]}kjfela}}}}}}}}" ::
      "{{{[}}}}dafda" :: "{{{{{{{{{}}}}}}}}}" ::
        "[[[[[[[[[kafjalfeianfailfeja;fjai;efa;sfj]]]]]]]]]kjajdain" :: "" ::
          "((((((fjdalfeja((((alefjalisj(())))))))))))d" :: ")))(((d" :: Nil) foreach test
}

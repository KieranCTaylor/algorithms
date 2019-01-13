object MergeSort {

  def merge(left: List[Int], right: List[Int]): List[Int] =
    (left, right) match {
      case(_, Nil) => left
      case(Nil, _) => right
      case(leftHead :: leftTail, rightHead :: rightTail) =>
        if (leftHead < rightHead) leftHead::merge(leftTail, right)
        else rightHead :: merge(left, rightTail)
    }

  def mergeSort(list: List[Int]): List[Int] = {
    val n = list.length / 2
    if (n == 0) list
    else {
      val (left, right) = list.splitAt(n)
      merge(mergeSort(left), mergeSort(right))
    }
  }

  mergeSort(List(33,44,22,-10,99))


    mergeSort(List())
}
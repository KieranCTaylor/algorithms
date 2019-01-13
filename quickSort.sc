val arr = List(3, 5, 11, 76, 4, 9)

def quickSort(xs: List[Int]): List[Int] = {
  val n = 1
  if (xs.length <= 1) xs
  else {
    val pivot = xs(n)
    val left: List[Int] = quickSort(xs.filter(x => pivot > x))
    val right: List[Int] = quickSort(xs.filter(x => pivot < x))
    val rightWithPivot = pivot :: right
    left ::: rightWithPivot
  }
}

quickSort(arr)
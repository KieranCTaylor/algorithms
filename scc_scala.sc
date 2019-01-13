import scala.io.Source

object Main extends App {

  def exploreForward(adjList: Map[Int, List[Int]], currentNode: Int,
                     foundNodes: Set[Int], finishingTime: List[Int]): (Set[Int], List[Int]) = {

    val crossOver: List[Int] = adjList(currentNode).filterNot(node => foundNodes.contains(node))

    if (crossOver.isEmpty) (foundNodes + currentNode, currentNode :: finishingTime)

    else exploreForward(adjList, crossOver.head, foundNodes + currentNode, finishingTime)

  }

  def searchFromStartNode(adjList: Map[Int, List[Int]], currentNode: Int,
                          foundThisPass: Set[Int], finishingTime: List[Int]): (Set[Int], List[Int]) = {

    val crossOver: List[Int] = adjList(currentNode).filterNot(node => foundThisPass.contains(node))

    if (crossOver.isEmpty) (foundThisPass + currentNode, currentNode :: finishingTime)

    else {
      val (downstreamFinds, downstreamFinishers) = exploreForward(adjList, crossOver.head, foundThisPass + currentNode, finishingTime)
      searchFromStartNode(adjList, currentNode, downstreamFinds, downstreamFinishers)
    }

  }


  def master_dfs(orderOfExecution: List[Int], adjList: Map[Int, List[Int]],
                 foundNodes: Set[Int], finishedList: List[Int], sccs: List[List[Int]]): (Set[Int], List[Int], List[List[Int]]) = {

    val (foundThisPass, finishers) = searchFromStartNode(adjList = adjList,
      currentNode = orderOfExecution.head, foundThisPass = foundNodes, finishingTime = finishedList)

    val scc: List[Int] = finishers.filterNot(node => finishedList.contains(node))

    val leftToExecute = orderOfExecution.filterNot(node => foundThisPass.contains(node))

    if (leftToExecute.isEmpty) (foundThisPass, finishers, scc :: sccs)

    else {
      master_dfs(orderOfExecution = leftToExecute, adjList = adjList,
        foundNodes = foundThisPass, finishedList = finishers, sccs = scc :: sccs)
    }

  }


  def readInputArray(path: String): List[List[Int]] = {

    val inputFile = Source.fromFile(path).getLines.toList.map(x => x.trim.split(" "))
    val numerated = inputFile.map(x => List(x(0).toInt, x(1).toInt))
    numerated
  }


  def toAdjList(inputArr: List[List[Int]]) = {

    var mappedInput: scala.collection.mutable.Map[Int, List[Int]] = scala.collection.mutable.Map()

    for (splitList <- inputArr) {
      if (mappedInput.keySet.contains(splitList.head)) mappedInput(splitList.head) = List(splitList.last) ::: mappedInput(splitList.head)
      else mappedInput(splitList.head) = List(splitList.last)
    }

    for (splitList <- inputArr) {
      if (!mappedInput.keySet.contains(splitList.last)) mappedInput(splitList.last) = List()
    }

    println("You've filled the map!")

    mappedInput.toMap
  }

  def maxSCCs(): Unit = {

    val inputArr = readInputArray("problem_files/SCC.txt")

    println("You've read in the input array!")

    val reversedInputArr = inputArr.map(x => x.reverse)

    val reverseInput = toAdjList(reversedInputArr)

    val secondOrderOfExecution: List[Int] = master_dfs(orderOfExecution = reverseInput.keys.toList.sorted.reverse, adjList = reverseInput,
      foundNodes = Set(), finishedList = List(), sccs = List())._2

    println("You've completed the first pass of the algorithm!")

    val outSCCs = master_dfs(orderOfExecution = secondOrderOfExecution, adjList = toAdjList(inputArr),
      foundNodes = Set(), finishedList = List(), sccs = List())._3

    val SCCLengths: List[Int] = outSCCs.map(x => x.length)

    println("5 largest SCC lengths are...")
    println(SCCLengths.sorted.reverse.slice(0, 5).mkString(", "))
  }

  maxSCCs()
}

import java.util.Scanner
import kotlin.math.*

private var n = ""
private var isVisited = mutableSetOf<Int>()
private var current = "".toMutableList()

private fun combination(
    startIndex: Int,
    selectedCount: Int,
    countToSelect: Int
) {
    if (selectedCount == countToSelect) {
        var currentAsString = ""
        current.forEach { currentAsString += it }
        isVisited.add(currentAsString.toInt())
    } else {
        for (i in startIndex .. n.length - (countToSelect - selectedCount)) {
            for (j in 0 .. current.size) {
                current.add(j, n[i])
                combination(i+1, selectedCount + 1, countToSelect)
                current.removeAt(j)
            }
        }
    }
}

private fun isPrime(number: Int): Boolean {
    if (number <= 1) return false

    for (i in 2 .. sqrt(number.toDouble()).toInt()) {
        if (number % i == 0) return false
    }
    return true
}

fun main() = with(Scanner(System.`in`)) {
    val c = nextInt()
    nextLine()
    for (i in 0 until c) {
        n = nextLine()

        var res = 0
        for (j in 1 .. n.length) {
            combination(0, 0, j)
        }
        isVisited.forEach {
            if (isPrime(it)) res += 1
        }
        isVisited.clear()

        println(res)
    }
}
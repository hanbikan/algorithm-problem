import java.util.*

private var N: Int? = null
private var M: Int? = null
private var K: Int? = null
private val oranges = mutableListOf<Int>()
private var dp: Array<Long>? = null

fun main() = with(Scanner(System.`in`)) {
    N = nextInt()
    M = nextInt()
    K = nextInt()
    oranges.add(0)
    for (i in 0 until N!!) oranges.add(nextInt())
    dp = Array(N!! + 1) { Long.MAX_VALUE }
    dp!![0] = 0

    for (start in 1 ..N!!) {
        var max = oranges[start].toLong()
        var min = oranges[start].toLong()

        for (count in 1 .. M!!) {
            val end = start+count-1
            if (end > N!!) break

            max = Math.max(max, oranges[end].toLong())
            min = Math.min(min, oranges[end].toLong())

            dp!![end] = Math.min(dp!![end], dp!![start-1] + K!! + count * (max - min))
        }
    }

    print(dp!![N!!])
}
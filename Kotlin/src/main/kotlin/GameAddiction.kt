import java.util.*

private var h = 0
private var n = 0
private val dx = listOf(1, 0)
private val dy = listOf(0, 1)
private var dp: Array<Array<Long>>? = null

private fun f(x: Int, y: Int): Long {
    if (x > n || y > n) return 0
    if (x == n && y == n) return 1

    if(dp!![x][y] == -1L){
        var res = 0L
        for(k in 0 until 2) {
            val nx = x + dx[k]
            val ny = y + dy[k]

            if(ny > nx) continue
            res += f(nx, ny)
        }
        dp!![x][y] = res
    }

    return dp!![x][y]
}

fun main() {
    val sc = Scanner(System.`in`)
    h = sc.nextInt()
    n = sc.nextInt()

    if(h > n) h = n.also { n = h }

    dp = Array(31) { Array(31) { -1L } }
    print(f(h, h).toString())
}

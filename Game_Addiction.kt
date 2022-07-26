import java.util.Scanner

var h = 0
var n = 0
val dx = listOf(1, 0)
val dy = listOf(0, 1)
var dp: Array<Array<Long>>? = null

fun f(x: Int, y: Int): Long {
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

    dp = Array(31, {Array(31, {-1L})})
    print(f(h, h).toString())
}
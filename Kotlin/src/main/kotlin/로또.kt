import java.util.Scanner

private var n = 0
private var m = 0

fun main() = with(Scanner(System.`in`)) {
    val t = nextInt()
    for (tc in 0 until t) {
        n = nextInt()
        m = nextInt()

        val dp = Array(n+1) { Array(m+1) { 0L } }

        for (j in 0 .. m) dp[0][j] = 1L
        for (i in 1 .. n) {
            for (j in 1 .. m) {
                dp[i][j] = dp[i-1][j/2] + dp[i][j-1]
            }
        }

        println(dp[n][m])
    }
}